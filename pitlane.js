(() => {
    const FALLBACK_DRIVERS = [
        ['Kimi Antonelli', 'Mercedes', 219],
        ['Lewis Hamilton', 'Ferrari', 169],
        ['George Russell', 'Mercedes', 160],
        ['Charles Leclerc', 'Ferrari', 138],
        ['Lando Norris', 'McLaren', 128],
        ['Max Verstappen', 'Red Bull Racing', 109],
        ['Oscar Piastri', 'McLaren', 92],
        ['Isack Hadjar', 'Red Bull Racing', 68],
        ['Liam Lawson', 'Racing Bulls', 43],
        ['Pierre Gasly', 'Alpine', 42],
        ['Arvid Lindblad', 'Racing Bulls', 23],
        ['Franco Colapinto', 'Alpine', 19],
        ['Oliver Bearman', 'Haas F1 Team', 18],
        ['Gabriel Bortoleto', 'Audi', 10],
        ['Carlos Sainz', 'Williams', 6],
        ['Alexander Albon', 'Williams', 5],
        ['Esteban Ocon', 'Haas F1 Team', 3],
        ['Nico Hulkenberg', 'Audi', 2],
        ['Fernando Alonso', 'Aston Martin', 1],
        ['Sergio Perez', 'Cadillac', 0],
        ['Valtteri Bottas', 'Cadillac', 0],
        ['Lance Stroll', 'Aston Martin', 0]
    ];

    const FALLBACK_TEAMS = [
        ['Mercedes', 379],
        ['Ferrari', 307],
        ['McLaren', 220],
        ['Red Bull Racing', 177],
        ['Racing Bulls', 66],
        ['Alpine', 61],
        ['Haas F1 Team', 21],
        ['Audi', 12],
        ['Williams', 11],
        ['Aston Martin', 1],
        ['Cadillac', 0]
    ];

    const slug = (name) => name.toLowerCase().replace(/[^a-z0-9]+/g, '-');

    function safeImg(url, fallback, alt) {
        const source = url || fallback;
        return `<img class="media-img" loading="lazy" src="${source}" alt="${alt}" onerror="this.onerror=null;this.src='${fallback}'">`;
    }

    async function getJSON(url) {
        const response = await fetch(url, { cache: 'no-store' });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        return response.json();
    }

    async function standings() {
        let drivers = FALLBACK_DRIVERS.map((driver, index) => ({
            pos: index + 1,
            name: driver[0],
            team: driver[1],
            points: driver[2]
        }));

        let teams = FALLBACK_TEAMS.map((team, index) => ({
            pos: index + 1,
            name: team[0],
            points: team[1]
        }));

        let source = 'Fallback snapshot';

        try {
            const [driverData, constructorData] = await Promise.all([
                getJSON('https://api.jolpi.ca/ergast/f1/2026/driverstandings/'),
                getJSON('https://api.jolpi.ca/ergast/f1/2026/constructorstandings/')
            ]);

            const driverList = driverData.MRData.StandingsTable.StandingsLists?.[0]?.DriverStandings || [];
            const constructorList = constructorData.MRData.StandingsTable.StandingsLists?.[0]?.ConstructorStandings || [];

            if (driverList.length) {
                drivers = driverList.map((entry) => ({
                    pos: Number(entry.position),
                    name: `${entry.Driver.givenName} ${entry.Driver.familyName}`,
                    team: entry.Constructors?.[0]?.name || '',
                    points: Number(entry.points)
                }));
            }

            if (constructorList.length) {
                teams = constructorList.map((entry) => ({
                    pos: Number(entry.position),
                    name: entry.Constructor.name,
                    points: Number(entry.points)
                }));
            }

            source = 'Live championship API';
        } catch (error) {
            console.warn('Standings API unavailable; using snapshot.', error);
        }

        return { drivers, teams, source };
    }

    function tableRows(rows, type) {
        return rows
            .map((row, index) => {
                const teamCell = type === 'drivers'
                    ? `<td>${row.team}</td>`
                    : '';

                return `<tr>
                    <td>${row.pos || index + 1}</td>
                    <td><strong>${row.name}</strong></td>
                    ${teamCell}
                    <td><strong>${row.points}</strong></td>
                </tr>`;
            })
            .join('');
    }

    async function renderStandings() {
        const driverBody = document.querySelector('#driver-standings-body');
        const constructorBody = document.querySelector('#constructor-standings-body');
        const status = document.querySelector('#standings-status');

        if (!driverBody && !constructorBody) {
            return;
        }

        const currentStandings = await standings();

        if (driverBody) {
            driverBody.innerHTML = tableRows(currentStandings.drivers, 'drivers');
        }

        if (constructorBody) {
            constructorBody.innerHTML = tableRows(currentStandings.teams, 'constructors');
        }

        if (status) {
            status.textContent = `${currentStandings.source} • refreshes automatically after new race results are published`;
        }
    }

    function teamCard(team, standingsMap) {
        const points = standingsMap[team.name] ?? 0;
        const fallback = `assets/${team.id}-fallback.svg`;
        const driverNames = team.drivers
            .map((driver) => `<span>${driver[0]}</span>`)
            .join('');

        return `<article class="team-card">
            <div class="team-card-media">
                ${safeImg(team.image, fallback, `${team.name} ${team.car}`)}
                <span class="team-badge">2026</span>
            </div>
            <div class="team-card-body">
                <div class="eyebrow">${team.full}</div>
                <h3>${team.name}</h3>
                <div class="team-meta">
                    <span>${team.car}</span>
                    <span>${points} PTS</span>
                </div>
                <div class="drivers-mini">${driverNames}</div>
                <a class="team-btn" href="${team.page}">Explore team →</a>
            </div>
        </article>`;
    }

    async function renderTeams() {
        const grid = document.querySelector('#teams-grid');

        if (!grid || !window.PITLANE_TEAMS) {
            return;
        }

        const currentStandings = await standings();
        const standingsMap = Object.fromEntries(
            currentStandings.teams.map((team) => [team.name, team.points])
        );

        grid.innerHTML = window.PITLANE_TEAMS
            .map((team) => teamCard(team, standingsMap))
            .join('');
    }

    function renderTeamPage() {
        const mount = document.querySelector('#team-page');

        if (!mount || !window.PITLANE_TEAMS) {
            return;
        }

        const teamId = mount.dataset.team;
        const team = window.PITLANE_TEAMS.find((item) => item.id === teamId);

        if (!team) {
            return;
        }

        const driverImages = window.PITLANE_DRIVER_IMAGES || {};
        const teamFallback = `assets/${team.id}-fallback.svg`;
        const driverPanels = team.drivers
            .map((driver) => {
                const name = driver[0];
                const fallback = `assets/${slug(name)}.svg`;
                const image = safeImg(driverImages[name], fallback, name);

                return `<article class="driver-panel">
                    ${image}
                    <div class="driver-info">
                        <span class="driver-number">#${driver[1]}</span>
                        <h3>${name}</h3>
                        <p>${driver[2]}</p>
                    </div>
                </article>`;
            })
            .join('');

        mount.innerHTML = `<section class="team-hero">
            <div class="container">
                <div class="team-hero-copy">
                    <span class="hero-kicker">2026 CONSTRUCTOR</span>
                    <h1>${team.name}</h1>
                    <p>${team.full}</p>
                    <div class="hero-pills">
                        <span>${team.car}</span>
                        <span>Drivers: ${team.drivers.map((driver) => driver[0]).join(' & ')}</span>
                    </div>
                </div>
                <div class="hero-car">
                    ${safeImg(team.image, teamFallback, team.car)}
                </div>
            </div>
        </section>
        <section class="container team-detail">
            <div class="section-head">
                <div>
                    <span class="eyebrow">THE GARAGE</span>
                    <h2>${team.car}</h2>
                </div>
                <a class="ghost-btn" href="index.html#teams">← All teams</a>
            </div>
            <div class="driver-grid">${driverPanels}</div>
            <div class="team-stats-grid">
                <div><small>CAR</small><strong>${team.car}</strong></div>
                <div><small>POWER ERA</small><strong>2026 GEN</strong></div>
                <div><small>DRIVERS</small><strong>${team.drivers.length}</strong></div>
                <div><small>STATUS</small><strong>ACTIVE</strong></div>
            </div>
        </section>`;
    }

    window.addEventListener('DOMContentLoaded', () => {
        renderStandings();
        renderTeams();
        renderTeamPage();
    });
})();
