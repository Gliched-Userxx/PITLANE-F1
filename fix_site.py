from pathlib import Path

root = Path(r'd:\IT VEDANT PROJECT\PITLANE F1')

css = r"""/* ==========================
   PITLANE F1 - PREMIUM STYLE
   ========================== */

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800&display=swap');

:root {
    --accent: #e10600;
    --surface: #090909;
    --surface-strong: #0c0c0c;
    --text: #f5f5f5;
    --muted: #c7c7c7;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    min-height: 100%;
    background: radial-gradient(circle at top center, rgba(225, 16, 0, 0.16), transparent 18%), #050505;
    color: var(--text);
    font-family: 'Orbitron', sans-serif;
    overflow-x: hidden;
}

body::before {
    content: '';
    position: fixed;
    inset: 0;
    background: radial-gradient(circle at top, rgba(255,255,255,.03), transparent 25%),
                radial-gradient(circle at 20% 10%, rgba(225,6,0,.08), transparent 10%),
                radial-gradient(circle at 80% 20%, rgba(255,255,255,.04), transparent 10%);
    pointer-events: none;
    z-index: -1;
}

a {
    color: inherit;
    text-decoration: none;
}

button,
.btn {
    transition: all .3s ease;
}

.navbar {
    background: rgba(0, 0, 0, 0.96);
    border-bottom: 2px solid var(--accent);
    padding: 1rem 2rem;
    position: sticky;
    top: 0;
    z-index: 999;
}

.navbar-brand {
    font-size: 1.9rem;
    font-weight: 800;
    letter-spacing: 0.16rem;
    color: var(--accent) !important;
}

.navbar-nav .nav-link {
    color: var(--text) !important;
    font-weight: 700;
    margin-left: 1rem;
}

.navbar-nav .nav-link:hover,
.navbar-nav .nav-link:focus {
    color: var(--accent) !important;
}

.dropdown-menu {
    background: #111;
    border: 1px solid var(--accent);
}

.dropdown-item {
    color: var(--text);
}

.dropdown-item:hover {
    background: var(--accent);
    color: #050505;
}

.hero {
    min-height: 90vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    background:
        linear-gradient(180deg, rgba(0,0,0,0.6), rgba(0,0,0,0.94)),
        url('https://images.unsplash.com/photo-1571260899304-425eee4c7efc?auto=format&fit=crop&w=1600&q=80');
    background-size: cover;
    background-position: center;
    padding: 3rem 1rem;
    position: relative;
}

.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at top, rgba(225,6,0,.18), transparent 22%),
                linear-gradient(180deg, rgba(0,0,0,.25), rgba(0,0,0,.9));
    pointer-events: none;
}

.hero .container {
    position: relative;
    z-index: 1;
}

.hero-label {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--accent);
    color: #050505;
    padding: 0.95rem 1.6rem;
    border-radius: 999px;
    font-weight: 700;
    margin-bottom: 1.5rem;
}

.hero h1 {
    font-size: 4rem;
    font-weight: 800;
    letter-spacing: 0.18rem;
    margin-bottom: 1rem;
    color: #fff;
    text-transform: uppercase;
    text-shadow: 0 0 40px rgba(225,6,0,.35);
    animation: glow 3.2s ease-in-out infinite alternate;
}

.hero p {
    font-size: 1.15rem;
    max-width: 760px;
    margin: 0 auto 2rem;
    color: #d7d7d7;
    line-height: 1.75;
}

.hero .btn {
    background: var(--accent);
    border: none;
    padding: 1rem 2.3rem;
    border-radius: 999px;
    font-weight: 700;
    color: #050505;
}

.hero .btn:hover {
    transform: translateY(-2px);
    background: #fff;
    color: var(--accent);
}

.main-title,
.section-title {
    text-align: center;
    font-size: 2.8rem;
    font-weight: 800;
    margin-bottom: 1.5rem;
    color: #fff;
    letter-spacing: 0.08rem;
    text-transform: uppercase;
}

.main-title::after,
.section-title::after {
    content: '';
    width: 110px;
    height: 4px;
    background: var(--accent);
    display: block;
    margin: 1rem auto 0;
    border-radius: 999px;
}

#teams {
    padding: 4rem 0 6rem;
}

.info-section {
    padding: 4rem 0;
}

.info-card {
    background: rgba(17,17,17,.96);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 24px;
    padding: 2rem;
    min-height: 220px;
    box-shadow: 0 20px 50px rgba(0,0,0,.2);
}

.info-card h3 {
    margin-bottom: 1rem;
    color: #fff;
}

.info-card p {
    color: #d2d2d2;
    line-height: 1.8;
}

.card {
    background: #111 !important;
    border: none !important;
    border-top: 4px solid var(--accent);
    border-radius: 24px;
    overflow: hidden;
    transition: transform .35s ease, box-shadow .35s ease;
    height: 100%;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 28px 60px rgba(225,6,0,.2);
}

.card-img-top,
.card img {
    height: 240px;
    object-fit: contain;
    padding: 1.5rem;
    background: #fff;
}

.card-body {
    padding: 2rem;
}

.card-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #fff;
}

.card-text {
    color: #d2d2d2;
    margin: 0.8rem 0 1rem;
}

.card .btn {
    background: var(--accent);
    border: none;
    padding: 0.95rem 1.8rem;
    border-radius: 999px;
    font-weight: 700;
    color: #050505;
}

.card .btn:hover {
    background: #fff;
    color: var(--accent);
}

.team-page {
    padding: 5rem 0;
}

.team-content {
    max-width: 960px;
    margin: 0 auto;
    background: rgba(17,17,17,.96);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 32px;
    padding: 3rem;
    box-shadow: 0 28px 65px rgba(0,0,0,.25);
}

.team-title {
    font-size: 3.4rem;
    margin-bottom: 0.7rem;
    color: #fff;
}

.team-image {
    width: 100%;
    border-radius: 26px;
    margin: 2rem 0;
    box-shadow: 0 24px 60px rgba(0,0,0,.25);
}

.team-copy {
    color: #d7d7d7;
    font-size: 1.05rem;
    line-height: 1.85;
    margin-bottom: 1.75rem;
}

.team-subtitle {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: var(--accent);
    text-transform: uppercase;
}

.driver-card {
    background: #111;
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 24px;
    overflow: hidden;
    transition: transform .3s ease, box-shadow .3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.driver-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 24px 60px rgba(225,6,0,.22);
}

.driver-card img {
    width: 100%;
    min-height: 300px;
    object-fit: cover;
}

.driver-content {
    padding: 1.7rem;
}

.stats {
    padding: 4rem 0;
    background: #090909;
}

.stat-box {
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 24px;
    padding: 2rem 1.5rem;
    text-align: center;
}

.stat-box h1 {
    font-size: 3.6rem;
    color: var(--accent);
    margin-bottom: 0.5rem;
}

.stat-box p {
    color: #d2d2d2;
    margin: 0;
}

.footer {
    background: #050505;
    border-top: 2px solid var(--accent);
    padding: 1.5rem 1rem;
    text-align: center;
    color: #c7c7c7;
}

.footer p {
    margin: 0;
}

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #111;
}

::-webkit-scrollbar-thumb {
    background: var(--accent);
    border-radius: 10px;
}

@keyframes glow {
    from { text-shadow: 0 0 20px rgba(225,6,0,.35); }
    to { text-shadow: 0 0 45px rgba(225,6,0,.55); }
}

@media (max-width: 992px) {
    .hero h1 { font-size: 3.1rem; }
    .main-title, .section-title { font-size: 2.4rem; }
}

@media (max-width: 768px) {
    .navbar { padding: 1rem 1rem; }
    .hero { min-height: 70vh; padding: 2.5rem 1rem; }
    .hero h1 { font-size: 2.5rem; }
    .hero p { font-size: 1rem; }
    .card-img-top { height: 180px; }
    .team-content { padding: 2rem; }
    .team-image { margin: 1.5rem 0; }
    .driver-card img { min-height: 240px; }
}
"""

base_team = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PITLANE F1 | {page_title}</title>
    <link rel="icon" href="https://cdn-icons-png.flaticon.com/128/1023/1023757.png">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="f1.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="index.html">⚡ PITLANE F1</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                    <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link" href="https://www.formula1.com" target="_blank">F1 Official</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <section class="team-page">
        <div class="team-content">
            <h1 class="team-title">{team_title}</h1>
            <h2 class="section-title">{car_name}</h2>
            <img src="{image}" alt="{car_name}" class="team-image">
            <p class="team-copy">{team_copy}</p>
            <div class="row g-4">
{driver_cards}
            </div>
        </div>
    </section>

    <footer class="footer">
        <p>© 2026 PITLANE F1 • All Rights Reserved</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
</body>
</html>
"""

def driver_card(name, image, bio):
    return f"""                <div class=\"col-md-6\">\n                    <div class=\"driver-card\">\n                        <img src=\"{image}\" alt=\"{name}\">\n                        <div class=\"driver-content\">\n                            <h3 class=\"team-subtitle\">{name}</h3>\n                            <p class=\"team-copy\">{bio}</p>\n                        </div>\n                    </div>\n                </div>\n"""

teams = [
    {
        'filename': 'audi.html',
        'page_title': 'Audi F1 Team',
        'team_title': 'Audi F1 Team',
        'car_name': 'R26',
        'image': 'https://bav-app-files.s3.ap-south-1.amazonaws.com/public-files/a260044-web-2880-jpg-1768985995-KfiAnkVlJSuOA6eHuLDJ',
        'team_copy': 'The Audi R26 is Audi\'s first works Formula 1 car for the 2026 era, built to deliver straight-line speed and high-efficiency hybrid performance.',
        'drivers': [
            ('Nico Hülkenberg', 'https://cdn-9.motorsport.com/images/mgl/63QmpND2/s8/nico-hulkenberg-audi-f1-team.jpg', 'A veteran driver known for his consistency and technical feedback, Nico brings stability to Audi\'s debut season.'),
            ('Gabriel Bortoleto', 'https://media.formula1.com/image/upload/t_16by9Centre/c_lfill,w_3392/q_auto/v1740000000/trackside-images/2026/F1_Grand_Prix_Of_Australia___Practice/2265042602.webp', 'A rising Brazilian talent with strong racecraft, Gabriel joins Audi as one of the most promising young drivers on the grid.'),
        ],
    },
    {
        'filename': 'cadillac.html',
        'page_title': 'Cadillac F1 Team',
        'team_title': 'Cadillac F1 Team',
        'car_name': 'MAC-26',
        'image': 'https://d3cm515ijfiu6w.cloudfront.net/wp-content/uploads/2026/02/27181126/sergio-perez-cadillac-bahrain-test-2026-planetf1-1320x742.jpg',
        'team_copy': 'The Cadillac MAC-26 is Cadillac\'s first Formula 1 challenger, designed to bring the American brand into the top class with hybrid power and bold style.',
        'drivers': [
            ('Valtteri Bottas', 'https://www.motorsportweek.com/wp-content/uploads/2026/01/Valtteri-Bottas-Cadillac-F1-2026.webp', 'A steady veteran who provides technical strength and measured race pace to the new Cadillac entry.'),
            ('Sergio Pérez', 'https://i0.wp.com/thejudge13.com/wp-content/uploads/2025/03/perez-cadlllac.webp', 'A seasoned strategist with strong tyre management, Sergio brings experience and racecraft to Cadillac.'),
        ],
    },
    {
        'filename': 'haas.html',
        'page_title': 'Haas F1 Team',
        'team_title': 'Haas F1 Team',
        'car_name': 'VF-26',
        'image': 'https://media.formula1.com/image/upload/q_auto/f_auto/v1737639848/fom-website/2026/Bahrain%20GP/Haas.webp',
        'team_copy': 'The Haas VF-26 is built for wheel-to-wheel racing in the compact 2026 era, blending aggressive aero with a Ferrari-backed power unit.',
        'drivers': [
            ('Esteban Ocon', 'https://www.autohebdo.fr/app/uploads/2025/11/DPPI_00125026_1234-2-753x494.jpg', 'A determined and experienced driver, Esteban provides Haas with strong defensive pace and consistency.'),
            ('Oliver Bearman', 'https://cdn.racingnews365.com/2025/Bearman/Bearman-Presser-Zandvoort.jpg?v=1756391012&width=1092&height=683&quality=85&crop=6000%2C3753%2C0%2C123', 'A young rising star with raw speed and potential, Oliver brings fresh energy to the lineup.'),
        ],
    },
    {
        'filename': 'visacprb.html',
        'page_title': 'Visa CashApp Racing Bulls',
        'team_title': 'Visa CashApp Racing Bulls',
        'car_name': 'VCARB 02',
        'image': 'https://www.racecar-engineering.com/wp-content/uploads/2025/02/SI202502180805_hires_jpeg_24bit_rgb.jpg',
        'team_copy': 'The VCARB 02 is the Bulls\' hybrid challenger, combining Red Bull speed with racing innovation for the 2026 midfield fight.',
        'drivers': [
            ('Arvid Lindblad', 'https://media.formula1.com/image/upload/t_16by9North/c_lfill,w_3392/q_auto/v1740000000/trackside-images/2025/Formula_1_Testing_in_Abu_Dhabi/2250864781.webp', 'A confident rookie with pace and ambition, Arvid is the future-facing driver in the Bulls garage.'),
            ('Liam Lawson', 'https://media.formula1.com/image/upload/t_16by9North/c_lfill,w_3392/q_auto/v1740000000/trackside-images/2025/F1_Grand_Prix_of_Hungary/2228284915.webp', 'A bold and aggressive racer, Liam is known for late moves and strong midfield battles.'),
        ],
    },
    {
        'filename': 'williams.html',
        'page_title': 'Williams Racing',
        'team_title': 'Williams Racing',
        'car_name': 'FW48',
        'image': 'https://r.testifier.nl/Acbs8526SDKI/resizing_type:fit/width:3840/height:2560/plain/https://s3-newsifier.ams3.digitaloceanspaces.com/gpblog.com/images/2026-02/fhigh-v4-sainz-169-mbgslvu9-20260203100643-6981ff7f004f3.jpg@webp',
        'team_copy': 'The Williams FW48 is engineered for stability and progress in the 2026 season, with a focus on aerodynamic control and race momentum.',
        'drivers': [
            ('Carlos Sainz Jr.', 'https://cdn-1.motorsport.com/images/amp/0L1NqoP2/s1000/carlos-sainz-williams.jpg', 'A seasoned race winner, Carlos brings intelligence and consistency to Williams.'),
            ('Alexander Albon', 'https://media.formula1.com/image/upload/t_16by9Centre/c_lfill,w_3392/q_auto/v1740000000/trackside-images/2024/F1_Grand_Prix_of_Canada___Qualifying/2156648602.webp', 'A strong midfield performer, Alexander offers solid pace and calm leadership on race day.'),
        ],
    },
    {
        'filename': 'alpine.html',
        'page_title': 'BWT Alpine',
        'team_title': 'BWT Alpine',
        'car_name': 'A526',
        'image': 'https://cdn.dribbble.com/users/503120/screenshots/14236421/media/5e1e9926259bbc5f3731b559c79dc3b1.png',
        'team_copy': 'The Alpine A526 is the French team\'s 2026 contender, crafted for agility and strategic performance through the midfield fight.',
        'drivers': [
            ('Pierre Gasly', 'https://media.formula1.com/image/upload/t_16by9North/c_lfill,w_3392/q_auto/v1740000000/trackside-images/2026/France/Pierre-Gasly.jpg', 'A clever and aggressive driver, Pierre combines experience with strong tyre management.'),
            ('Esteban Ocon', 'https://media.formula1.com/image/upload/t_16by9North/c_lfill,w_3392/q_auto/v1740000000/France/Ocon.jpg', 'A determined racer with excellent racecraft, Esteban delivers consistent midfield results.'),
        ],
    },
    {
        'filename': 'AstonMartin.html',
        'page_title': 'Aston Martin Aramco F1',
        'team_title': 'Aston Martin Aramco F1',
        'car_name': 'AMR26',
        'image': 'https://www.astonmartin.com/-/media/amr26/amr26-hero.jpg?mw=1920&rev=147dd8bb3a4c4823b62a8ec77af16277&hash=9B1BEDA5765AC9B2E4806DC5603131C0',
        'team_copy': 'The AMR26 is Aston Martin\'s 2026 package, built for the new era with Honda hybrid support and a bold works program.',
        'drivers': [
            ('Fernando Alonso', 'https://media.formula1.com/image/upload/c_lfill,w_2048/q_auto/v1740000000/fom-website/2026/Australia/Alonso%20Australia%202026.webp', 'A legendary racer with unmatched racecraft, Fernando brings experience and determination to the team.'),
            ('Lance Stroll', 'https://media.formula1.com/image/upload/t_16by9North/c_lfill,w_3392/q_auto/v1740000000/fom-website/2023/Aston%20Martin/GettyImages-1806661948.webp', 'A skilled driver on his home team, Lance combines speed with strong car control in variable conditions.'),
        ],
    },
    {
        'filename': 'Ferrari.html',
        'page_title': 'Scuderia Ferrari',
        'team_title': 'Scuderia Ferrari',
        'car_name': 'SF-26',
        'image': 'https://preview.redd.it/the-ferrari-sf-26-livery-v0-hra25jk3u2fg1.png?width=640&crop=smart&auto=webp&s=5cf50be3b7579b819712d1c39917b65eb85e8480',
        'team_copy': 'The Ferrari SF-26 is the latest entry from the storied Italian team, engineered for championship pace and aerodynamic precision.',
        'drivers': [
            ('Lewis Hamilton', 'https://sportsbase.io/images/gpfans/copy_1200x800/ea02da98bfaee5db0c846711a0763e0007008a99.jpg', 'The seven-time world champion brings relentless speed and experience to Ferrari.'),
            ('Charles Leclerc', 'https://www.autohebdo.fr/app/uploads/2025/12/charles-leclerc-ferrari-abu-dhabi.jpg', 'A qualifying specialist and team leader, Charles is Ferrari\'s top contender for race wins.'),
        ],
    },
    {
        'filename': 'Mclaren.html',
        'page_title': 'McLaren Mercedes',
        'team_title': 'McLaren Mercedes',
        'car_name': 'MCL40',
        'image': 'https://upload.wikimedia.org/wikipedia/commons/2/27/McLaren_MCL40_of_Oscar_Piastri_%28028A8060%29.jpg',
        'team_copy': 'The McLaren MCL40 combines championship momentum with a fresh aerodynamic approach for the 2026 World Championship.',
        'drivers': [
            ('Oscar Piastri', 'https://media.formula1.com/image/upload/t_16by9North/c_lfill,w_3392/q_auto/v1740000000/trackside-images/2026/F1_Grand_Prix_Of_China___Previews/2266070615.webp', 'A rapidly rising star, Oscar delivers strong pace and maturity beyond his years.'),
            ('Lando Norris', 'https://e0.365dm.com/25/05/768x432/skysports-lando-norris-mclaren_6902932.jpg?20250501201310', 'A crowd favorite with sharp overtaking ability, Lando is the team\'s emotional leader and fast qualifier.'),
        ],
    },
    {
        'filename': 'Mercedes.html',
        'page_title': 'Mercedes AMG Petronas',
        'team_title': 'Mercedes AMG Petronas',
        'car_name': 'W17',
        'image': 'https://media.formula1.com/image/upload/c_lfill,w_3392/q_auto/v1740000000/fom-website/2026/Mercedes/Mercedes-AMG%20F1%20W17%20E%20PERFORMANCE%20-%20GR%204.webp',
        'team_copy': 'The Mercedes W17 continues the Silver Arrows legacy with advanced hybrid systems and aerodynamic refinement.',
        'drivers': [
            ('George Russell', 'https://www.telegraph.co.uk/content/dam/formula-1/2025/03/21/TELEMMGLPICT000417235519_17425744209370_trans_NvBQzQNjv4BqqVzuuqpFlyLIwiB6NTmJwfSVWeZ_vEN7c6bHu2jJnT8.jpeg?imwidth=640', 'A precise and fast driver, George leads Mercedes as a championship contender.'),
            ('Andrea Kimi Antonelli', 'https://www.aljazeera.com/wp-content/uploads/2026/03/AFP__20260315__A3BG8LG__v1__HighRes__AutoPrixF1ChnPodium-1773567065.jpg?resize=770%2C513&quality=80', 'A brilliant young talent, Andrea brings raw speed and future star potential to the team.'),
        ],
    },
    {
        'filename': 'RedBull.html',
        'page_title': 'Oracle Red Bull Racing',
        'team_title': 'Oracle Red Bull Racing',
        'car_name': 'RB26',
        'image': 'https://pngimg.com/uploads/red_bull/small/red_bull_PNG12.png',
        'team_copy': 'The RB26 is Red Bull\'s championship-focused machine, designed to dominate the 2026 technical regulations with supreme aerodynamics.',
        'drivers': [
            ('Max Verstappen', 'https://media.formula1.com/image/upload/t_16by9North/c_lfill,w_3392/q_auto/v1740000000/trackside-images/2025/Belgium/Max-Verstappen.jpg', 'A dominant champion with relentless pace, Max pushes the RB26 to its limit every race weekend.'),
            ('Sergio Pérez', 'https://media.formula1.com/image/upload/t_16by9North/c_lfill,w_3392/q_auto/v1740000000/trackside-images/2025/Spa/Perez.jpg', 'A strategic racer with strong tyre management, Sergio is the perfect second weapon for Red Bull.'),
        ],
    },
]

index = r"""<!doctype html>
<html lang="en">
    <head>
        <title>PITLANE F1 | Home</title>
        <link rel="icon" href="https://cdn-icons-png.flaticon.com/128/1023/1023757.png">
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous" />
        <link rel="stylesheet" href="f1.css">
    </head>

    <body>
        <header>
            <nav class="navbar navbar-expand-lg navbar-dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="index.html">⚡ PITLANE F1</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <li class="nav-item"><a class="nav-link" href="https://www.formula1.com" target="_blank">F1 Official</a></li>
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">Follow Us</a>
                                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <li><a class="dropdown-item" href="https://www.instagram.com/f1" target="_blank">Instagram</a></li>
                                    <li><a class="dropdown-item" href="https://www.youtube.com/@Formula1" target="_blank">YouTube</a></li>
                                    <li><a class="dropdown-item" href="https://x.com/F1" target="_blank">X (Twitter)</a></li>
                                    <li><a class="dropdown-item" href="https://www.facebook.com/Formula1" target="_blank">Facebook</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>

        <main>
            <section class="hero">
                <div class="container">
                    <div class="hero-label">🏁 Welcome to the Pit Lane</div>
                    <h1>Formula 1 Teams 2026</h1>
                    <p>Explore the 2026 grid with team profiles, driver lineups, and an F1-inspired design that brings the paddock to life.</p>
                    <a href="#teams"><button class="btn btn-primary">Explore Teams</button></a>
                </div>
            </section>

            <section id="teams" class="container mt-5">
                <h2 class="main-title">Featured Teams</h2>
                <div class="row g-4">
                    <div class="col-md-4"><div class="card shadow"><img src="https://pngimg.com/uploads/red_bull/small/red_bull_PNG12.png" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Red Bull RB26</h5><p class="card-text">Oracle Red Bull Racing</p><a href="RedBull.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://pngimg.com/uploads/ferrari/small/ferrari_PNG10665.png" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Ferrari SF-26</h5><p class="card-text">Scuderia Ferrari</p><a href="Ferrari.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://pngimg.com/uploads/mercedes_logos/small/mercedes_logos_PNG1.png" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Mercedes W17</h5><p class="card-text">Mercedes AMG Petronas</p><a href="Mercedes.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://pngimg.com/uploads/Mclaren/small/Mclaren_PNG19.png" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">McLaren MCL40</h5><p class="card-text">McLaren Mercedes</p><a href="Mclaren.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://pngimg.com/uploads/aston_martin/small/aston_martin_PNG48.png" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Aston Martin AMR26</h5><p class="card-text">Aston Martin Aramco</p><a href="AstonMartin.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://www.logo.wine/a/logo/Alpine_(automobile)/Alpine_(automobile)-Logo.wine.svg" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Alpine A526</h5><p class="card-text">BWT Alpine</p><a href="alpine.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://upload.wikimedia.org/wikipedia/commons/f/f9/Logo_Williams_F1.png" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Williams FW48</h5><p class="card-text">Williams Racing</p><a href="williams.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://www.nicepng.com/png/full/609-6091929_logo-haas-f1-haas-f1-logo.png" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Haas VF-26</h5><p class="card-text">Haas F1 Team</p><a href="haas.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://cdn.prod.website-files.com/61b372525d9e220633140352/65df7c39bce657df7423a0af_Visa_Cash_App_RB_team_logo.webp" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">VCARB 02</h5><p class="card-text">Visa CashApp Racing Bulls</p><a href="visacprb.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://upload.wikimedia.org/wikipedia/commons/9/92/Audi-Logo_2016.svg" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Audi R26</h5><p class="card-text">Audi F1 Team</p><a href="audi.html" class="btn btn-danger">About team</a></div></div></div>
                    <div class="col-md-4"><div class="card shadow"><img src="https://car-logos.b-cdn.net/wp-content/uploads/2023/05/cadillac-logo-2021-present-1024x742.webp" class="card-img-top"><div class="card-body text-center"><h5 class="card-title">Cadillac MAC-26</h5><p class="card-text">Cadillac F1 Team</p><a href="cadillac.html" class="btn btn-danger">About team</a></div></div></div>
                </div>
            </section>

            <section class="info-section">
                <div class="container">
                    <div class="row g-4 text-center">
                        <div class="col-md-4"><div class="info-card"><h3>Modern F1 Theme</h3><p>A sleek black and red look built to match the drama of Formula 1.</p></div></div>
                        <div class="col-md-4"><div class="info-card"><h3>Driver Lineups</h3><p>Each team page includes the car, the drivers and a premium grid-style profile.</p></div></div>
                        <div class="col-md-4"><div class="info-card"><h3>Responsive Layout</h3><p>Clean cards, bold hero styling, and mobile-friendly navigation make the site easier to explore.</p></div></div>
                    </div>
                </div>
            </section>
        </main>

        <footer class="footer mt-5 py-4 text-center">
            <p class="mb-0">© 2026 PITLANE F1 • All Rights Reserved • Formula 1 Teams Directory</p>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    </body>
</html>
"""

for team in teams:
    driver_cards = ''.join(driver_card(name, image, bio) for name, image, bio in team['drivers'])
    page = base_team.format(
        page_title=team['page_title'],
        team_title=team['team_title'],
        car_name=team['car_name'],
        image=team['image'],
        team_copy=team['team_copy'],
        driver_cards=driver_cards,
    )
    (root / team['filename']).write_text(page, encoding='utf-8')

(root / 'f1.css').write_text(css, encoding='utf-8')
(root / 'index.html').write_text(index, encoding='utf-8')

print('Rewrote all team pages, homepage, and stylesheet.')
