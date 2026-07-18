import os

OUT_DIR = "/home/claude/nora-site/pages"
os.makedirs(OUT_DIR, exist_ok=True)
EN_OUT_DIR = "/home/claude/nora-site/pages/en"
os.makedirs(EN_OUT_DIR, exist_ok=True)

IMG_B64 = {
    "cnc": "/assets/img/cnc.webp",
    "profile": "/assets/img/profile.webp",
    "laser": "/assets/img/laser.webp",
    "welded_pipe": "/assets/img/welded_pipe.webp",
    "tubes": "/assets/img/tubes.webp",
    "pipes": "/assets/img/pipes.webp",
    "plasma": "/assets/img/plasma.webp",
    "welded_fab": "/assets/img/welded_fab.webp",
    "seamless_pipe": "/assets/img/seamless_pipe.webp",
    "bars": "/assets/img/bars.webp",
    "cutbend": "/assets/img/cutbend.webp",
    "sheet": "/assets/img/sheet.webp",
}

PRODUCT_B64 = {
    "kutu_profil": "/assets/img/kutu_profil.webp",
    "metal_boru": "/assets/img/metal_boru.webp",
    "kosebent": "/assets/img/kosebent.webp",
    "lama_demiri": "/assets/img/lama_demiri.webp",
    "silme_demiri": "/assets/img/silme_demiri.webp",
    "npu_demiri": "/assets/img/npu_demiri.webp",
    "kare_demir": "/assets/img/kare_demir.webp",
    "t_demir": "/assets/img/t_demir.webp",
    "transmisyon_mili": "/assets/img/transmisyon_mili.webp",
    "sac_cesitleri": "/assets/img/sac_cesitleri.webp",
    "cati_panelleri": "/assets/img/cati_panelleri.webp",
    "cephe_panelleri": "/assets/img/cephe_panelleri.webp",
    "imalat_celigi": "/assets/img/imalat_celigi.webp",
    "islah_celigi": "/assets/img/islah_celigi.webp",
    "otomat_celigi": "/assets/img/otomat_celigi.webp",
    "sementasyon_celigi": "/assets/img/sementasyon_celigi.webp",
    "pas_sac_levha": "/assets/img/pas_sac_levha.webp",
    "pas_profil": "/assets/img/pas_profil.webp",
    "pas_lama": "/assets/img/pas_lama.webp",
    "pas_altikose": "/assets/img/pas_altikose.webp",
    "pas_dikisli_boru": "/assets/img/pas_dikisli_boru.webp",
    "pas_dikissiz_boru": "/assets/img/pas_dikissiz_boru.webp",
    "pas_cubuk_mil": "/assets/img/pas_cubuk_mil.webp",
    "pas_fittings": "/assets/img/pas_fittings.webp",
}

NEW_PRODUCT_IMAGES = {
    "shredder_knives": "/assets/img/shredder_knives.webp",
    "constr_bucket_grey1": "/assets/img/constr_bucket_grey1.webp",
    "constr_bucket_grey2": "/assets/img/constr_bucket_grey2.webp",
    "constr_bucket_black": "/assets/img/constr_bucket_black.webp",
    "constr_forks": "/assets/img/constr_forks.webp",
    "constr_arm": "/assets/img/constr_arm.webp",
    "constr_bucket_yellow": "/assets/img/constr_bucket_yellow.webp",
}

PRODUCT_B64.update(NEW_PRODUCT_IMAGES)

CERT_IMAGES = {
    "cert_iso9001": "/assets/img/cert_iso9001.webp",
    "cert_iso10002": "/assets/img/cert_iso10002.webp",
    "cert_iso14001": "/assets/img/cert_iso14001.webp",
    "cert_iso45001": "/assets/img/cert_iso45001.webp",
}

BANNER_IMAGES = {
    "about_building": "/assets/img/about_building.webp",
    "contact_gate": "/assets/img/contact_gate.webp",
}

NORA_LOGO_PATH = "/assets/img/nora-logo.webp"

STYLE = """
  :root{
    --ink:#0D0D0D;
    --ink2:#171717;
    --ink3:#1F1F1F;
    --coral:#BA0000;
    --lavender:#9A9A9A;
    --gray:#9A9A9A;
    --white:#FFFFFF;
  }
  *{box-sizing:border-box; margin:0; padding:0;}
  html{scroll-behavior:smooth;}
  html,body{background:var(--ink); color:var(--white); cursor:none;}
  body{
    font-family:'Poppins', sans-serif;
    overflow-x:hidden;
    animation:pageEnter .6s ease-out both;
  }
  @keyframes pageEnter{
    from{opacity:0;}
    to{opacity:1;}
  }
  @keyframes pageLeave{
    from{opacity:1;}
    to{opacity:0;}
  }
  body.page-leaving{
    animation:pageLeave .3s ease-out forwards;
    pointer-events:none;
  }
  @media (prefers-reduced-motion: reduce){
    body{animation:none;}
    body.page-leaving{animation:none;}
  }
  a, button{cursor:none;}
  .serif{font-family:'Jost', sans-serif;}
  h1,h2,h3{font-family:'Jost', sans-serif; font-weight:600; line-height:1.05; text-transform:uppercase; letter-spacing:0.01em;}
  a{color:inherit; text-decoration:none;}
  .wrap{max-width:1300px; margin:0 auto; padding:0 60px;}

  /* ---------- SCROLL REVEAL ---------- */
  .reveal{opacity:0; transform:translateY(36px); transition:opacity .8s cubic-bezier(.16,.84,.44,1), transform .8s cubic-bezier(.16,.84,.44,1);}
  .reveal.in{opacity:1; transform:translateY(0);}
  .reveal-stagger > *{opacity:0; transform:translateY(28px); transition:opacity .7s cubic-bezier(.16,.84,.44,1), transform .7s cubic-bezier(.16,.84,.44,1);}
  .reveal-stagger.in > *{opacity:1; transform:translateY(0);}
  .reveal-stagger.in > *:nth-child(1){transition-delay:.02s;}
  .reveal-stagger.in > *:nth-child(2){transition-delay:.09s;}
  .reveal-stagger.in > *:nth-child(3){transition-delay:.16s;}
  .reveal-stagger.in > *:nth-child(4){transition-delay:.23s;}
  .reveal-stagger.in > *:nth-child(5){transition-delay:.30s;}
  .reveal-stagger.in > *:nth-child(6){transition-delay:.37s;}
  @media (prefers-reduced-motion: reduce){
    .reveal, .reveal-stagger > *{opacity:1; transform:none; transition:none;}
  }

  /* ---------- CUSTOM CURSOR ---------- */
  #cursor{
    position:fixed; top:0; left:0; width:16px; height:16px; border-radius:50%;
    border:1.5px solid var(--white); pointer-events:none; z-index:9999;
    transform:translate(-50%,-50%); transition:width .25s, height .25s, background .25s, border-color .25s, opacity .2s;
    mix-blend-mode:difference; opacity:0;
  }
  #cursor.visible{opacity:1;}
  #cursor.grow{width:38px; height:38px; background:var(--white);}

  #dustCanvas{
    position:fixed; inset:0; z-index:55; pointer-events:none; opacity:0.5;
  }

  /* ---------- SOCIAL RAIL ---------- */
  .social-rail{
    position:fixed; left:14px; bottom:14px; z-index:95;
    display:flex; flex-direction:column-reverse; gap:8px;
  }
  .social-rail a{
    width:42px; height:42px; border-radius:50%; display:flex; align-items:center; justify-content:center;
    font-size:18px; color:var(--white); box-shadow:0 4px 14px rgba(0,0,0,0.35);
  }
  .social-rail a svg{width:17px; height:17px;}
  .social-rail a.phone{background:#3a3a3a;}
  .social-rail a.linkedin{background:#444444;}
  .social-rail a.whatsapp{background:#3a3a3a;}
  .social-rail a.instagram{background:#444444;}
  .social-rail a:hover{background:var(--coral);}

  /* ---------- TOP BAR ---------- */
  .topbar{
    position:fixed; top:0; left:0; right:0; z-index:85;
    display:flex; justify-content:space-between; align-items:center;
    padding:34px 80px; mix-blend-mode:normal; pointer-events:none;
  }
  .topbar .logo{pointer-events:auto;}
  .topbar .menu-btn{pointer-events:auto;}
  .topbar-right{display:flex; align-items:center; gap:14px; pointer-events:none;}
  .lang-dropdown{position:relative; pointer-events:auto;}
  .lang-current{
    font-family:'Poppins'; font-size:13px; font-weight:600; letter-spacing:0.08em;
    color:var(--white); background:none; border:1px solid rgba(255,255,255,0.35); border-radius:20px;
    padding:8px 16px; cursor:none; display:flex; align-items:center; gap:6px;
    transition:background .2s ease, border-color .2s ease;
  }
  .lang-current::after{content:'\u25be'; font-size:10px; transition:transform .25s ease;}
  .lang-dropdown.open .lang-current::after{transform:rotate(180deg);}
  .lang-current:hover{background:rgba(255,255,255,0.1); border-color:var(--coral);}
  .lang-options{
    position:absolute; top:calc(100% + 10px); right:0; z-index:120;
    background:var(--ink2); border:1px solid rgba(255,255,255,0.12); border-radius:14px;
    padding:6px; display:flex; flex-direction:column; gap:2px; min-width:120px;
    opacity:0; visibility:hidden; transform:translateY(-8px);
    transition:opacity .25s cubic-bezier(.4,0,.2,1), transform .25s cubic-bezier(.4,0,.2,1), visibility .25s;
    box-shadow:0 20px 40px rgba(0,0,0,0.4);
  }
  .lang-dropdown.open .lang-options{opacity:1; visibility:visible; transform:translateY(0);}
  .lang-options .lang-switch{
    display:block; font-family:'Poppins'; font-size:13px; font-weight:500; letter-spacing:0.04em;
    color:var(--white); padding:10px 14px; border-radius:9px; transition:background .2s ease, color .2s ease;
  }
  .lang-options .lang-switch:hover{background:rgba(255,255,255,0.08); color:var(--coral);}
  .logo{display:flex; align-items:center; gap:12px;}
  .logo-img{height:72px; width:auto; display:block;}
  .logo .mark{width:34px; height:34px; flex-shrink:0;}
  .logo .word{
    font-family:'Poppins'; font-weight:800; font-size:22px; letter-spacing:0.01em; color:var(--white);
  }
  .logo .tag{
    font-family:'Poppins'; font-weight:600; font-size:9px; letter-spacing:0.15em;
    color:var(--gray); text-transform:uppercase; display:block; margin-top:1px;
  }
  .menu-btn{
    width:52px; height:52px; display:flex; align-items:center; justify-content:center;
    background:none; border:none; color:var(--white); z-index:80; position:relative;
  }
  .menu-btn .bar{width:26px; height:2px; background:var(--white); position:relative; transition:background .2s;}
  .menu-btn .bar::before, .menu-btn .bar::after{
    content:''; position:absolute; left:0; width:26px; height:2px; background:var(--white);
    transition:transform .3s ease, top .3s ease;
  }
  .menu-btn .bar::before{top:-8px;}
  .menu-btn .bar::after{top:8px;}
  .menu-btn.open .bar{background:transparent;}
  .menu-btn.open .bar::before{top:0; transform:rotate(45deg);}
  .menu-btn.open .bar::after{top:0; transform:rotate(-45deg);}

  /* ---------- FULLSCREEN MENU ---------- */
  .fullmenu{
    position:fixed; inset:0; background:var(--ink); z-index:75;
    display:flex; flex-direction:column; justify-content:center;
    padding:0 60px 0 clamp(60px, 12vw, 200px); transform:translateX(100%); transition:transform .6s cubic-bezier(.65,0,.35,1);
  }
  .fullmenu.open{transform:translateX(0);}
  .menu-inner{width:100%; max-width:900px;}
  .menu-close{
    position:absolute; top:30px; right:32px; width:44px; height:44px;
    display:flex; align-items:center; justify-content:center;
    background:none; border:none; z-index:90; cursor:none;
  }
  .menu-list{list-style:none;}
  .menu-list > li{margin-bottom:6px;}
  .menu-item{
    font-family:'Jost'; font-size:clamp(28px,4vw,52px); font-weight:600;
    color:var(--gray); display:flex; align-items:center; gap:16px; padding:5px 0;
    transition:color .2s; cursor:none;
  }
  .menu-item:hover, .menu-item.active{color:var(--white);}
  .menu-item .chev{font-size:18px; transition:transform .3s;}
  .menu-item.active .chev{transform:rotate(180deg);}
  .submenu{
    list-style:none; max-height:0; overflow:hidden; transition:max-height .4s ease;
    padding-left:8px;
  }
  .submenu.open{max-height:600px;}
  .submenu li{padding:6px 0;}
  .submenu a{
    font-family:'Jost'; font-size:16px; font-weight:600; color:var(--lavender);
  }
  .submenu a:hover, .submenu a.active{color:var(--white);}
  .menu-social{
    position:absolute; bottom:36px; right:60px; display:flex; gap:24px;
  }
  .menu-social a{
    font-family:'Poppins'; font-size:11px; letter-spacing:0.12em; color:var(--gray); text-transform:uppercase;
  }
  .menu-social a:hover{color:var(--white);}

  /* ---------- HERO SLIDER (smooth horizontal slide, filmstrip-style) ---------- */
  .hero-spacer{ height:100vh; }
  .hero-fixed{
    position:fixed; inset:0; z-index:50; overflow:hidden; background:var(--ink);
    opacity:1; visibility:visible; transition:opacity .3s ease;
  }
  .hero-fixed.exited{ opacity:0; visibility:hidden; pointer-events:none; }
  .hero-viewport{ position:absolute; inset:0; overflow:hidden; direction:ltr; }
  .hero-track{
    position:absolute; top:0; left:0; height:100%; display:flex; align-items:stretch; direction:ltr;
    transition: transform .68s cubic-bezier(.65,0,.35,1);
    will-change: transform;
  }
  .hero-slide{
    position:relative; height:100%; flex:0 0 auto;
    background-size:cover; background-position:center;
    filter:blur(9px) brightness(0.45) saturate(1.05);
    transform:scale(1.05);
    transition: filter .68s cubic-bezier(.65,0,.35,1), transform .68s cubic-bezier(.65,0,.35,1), box-shadow .68s ease;
    cursor:none; pointer-events:none;
  }
  .hero-slide.active{
    filter:blur(0) brightness(1) saturate(1);
    transform:scale(1);
    box-shadow:0 40px 100px rgba(0,0,0,0.55);
    z-index:2; pointer-events:auto;
  }
  .hero-slide::after{
    content:''; position:absolute; inset:0;
    background:linear-gradient(0deg, rgba(10,10,16,0.5) 0%, transparent 40%);
    opacity:0; transition:opacity .68s ease;
  }
  .hero-slide.active::after{ opacity:1; }
  .slide-label{
    position:absolute; left:0; right:0; bottom:64px; z-index:6; text-align:center;
    pointer-events:none; opacity:1; transform:translateY(0);
    transition:opacity .4s cubic-bezier(.4,0,.2,1), transform .4s cubic-bezier(.22,.61,.36,1);
  }
  .hero-fixed.label-hidden .slide-label{ opacity:0; transform:translateY(14px); }
  .slide-eyebrow{
    font-family:'Poppins'; font-size:11px; letter-spacing:0.25em; text-transform:uppercase;
    color:var(--coral); margin-bottom:10px; font-weight:600;
  }
  .slide-label h1{
    font-family:'Poppins'; font-weight:700; font-size:clamp(22px,2.6vw,34px);
    letter-spacing:0.04em; text-transform:uppercase; color:var(--white); margin-bottom:12px;
  }
  .slide-rule{width:40px; height:3px; background:var(--coral); margin:0 auto;}
  .hero-dots{
    position:absolute; bottom:24px; right:36px; z-index:70; display:flex; flex-direction:row; gap:10px;
  }
  .dot{
    width:8px; height:8px; border-radius:50%; background:rgba(255,255,255,0.3);
    position:relative; transition:background .3s ease;
  }
  .dot.active{ background:var(--coral); }
  .dot.active::after{
    content:''; position:absolute; inset:-4px; border-radius:50%;
    border:1.5px solid var(--coral);
  }
  .scroll-hint{
    position:absolute; left:76px; bottom:24px; z-index:60;
    font-family:'Poppins'; font-size:11px; letter-spacing:0.15em; text-transform:uppercase;
    color:rgba(255,255,255,0.6); display:flex; align-items:center; gap:10px;
  }
  .scroll-hint .line{width:30px; height:1px; background:rgba(255,255,255,0.4); position:relative; overflow:hidden;}
  .scroll-hint .line::after{
    content:''; position:absolute; top:0; left:-30px; width:30px; height:100%; background:var(--coral);
    animation:scrollacross 1.8s ease-in-out infinite;
  }
  @keyframes scrollacross{ 0%{left:-30px;} 100%{left:30px;} }

  @keyframes kenburns{
    0%{ transform:scale(1.08); }
    100%{ transform:scale(1.18); }
  }
  .hero-slide{ animation:kenburns 14s ease-in-out infinite alternate; }

  /* ---------- SECTION TRANSITION BANNER (style like reference "Blog"/"Referanslar" pages) ---------- */
  .banner{
    position:relative; height:46vh; min-height:320px; display:flex; align-items:flex-end;
    background:radial-gradient(circle at 60% 30%, #2b2b2b, #0D0D0D 70%);
    overflow:hidden;
  }
  .banner::after{
    content:''; position:absolute; inset:0;
    background:linear-gradient(0deg, rgba(10,10,16,0.9), rgba(10,10,16,0.2));
  }
  .banner-content{position:relative; z-index:2; padding:0 60px 44px;}
  .banner h2{font-size:clamp(42px,6vw,90px); color:var(--white);}

  /* ---------- SERVICES SECTION ---------- */
  .section{padding:110px 0;}
  .section-eyebrow{
    font-family:'Poppins'; font-size:12px; letter-spacing:0.2em; text-transform:uppercase;
    color:var(--coral); margin-bottom:16px; font-weight:600;
  }
  .section-title{font-size:clamp(30px,4vw,50px); color:var(--white); margin-bottom:50px; max-width:640px;}

  .service-grid{
    display:grid; grid-template-columns:repeat(3, 1fr); gap:1px; background:rgba(255,255,255,0.08);
  }
  .service-card{
    background:var(--ink2); transition:background .3s; overflow:hidden;
  }
  .service-card:hover{background:var(--ink3);}
  .service-card .thumb{
    height:190px; background-size:cover; background-position:center; filter:grayscale(0.15);
  }
  .service-card .body{padding:30px 30px 34px;}
  .service-card .idx{
    font-family:'Poppins'; font-size:12px; color:var(--coral); letter-spacing:0.1em; margin-bottom:14px; display:block;
  }
  .service-card h3{font-family:'Jost'; font-size:24px; color:var(--white); margin-bottom:14px; font-weight:600;}
  .service-card p{font-family:'Poppins'; font-size:14px; color:var(--gray); line-height:1.7;}
  .more{
    display:inline-block; font-family:'Poppins'; font-size:11px;
    letter-spacing:0.1em; text-transform:uppercase; color:var(--white);
    border:1px solid var(--coral); padding:10px 18px;
    transition:background .35s cubic-bezier(.4,0,.2,1), transform .35s cubic-bezier(.4,0,.2,1), border-color .35s ease;
  }
  .more:hover{background:var(--coral); transform:translateX(4px);}
  .service-card .more{
    display:inline-block; margin-top:20px; font-family:'Poppins'; font-size:11px;
    letter-spacing:0.1em; text-transform:uppercase; color:var(--white);
    border:1px solid var(--coral); padding:10px 18px;
    transition:background .35s cubic-bezier(.4,0,.2,1), transform .35s cubic-bezier(.4,0,.2,1), border-color .35s ease;
  }
  .service-card .more:hover{background:var(--coral); transform:translateX(4px);}

  /* ---------- SERVICE DETAIL PAGE ---------- */
  .service-detail-grid{
    display:grid; grid-template-columns:2fr 1fr; gap:50px; align-items:start;
  }
  .service-detail-hero{
    width:100%; height:340px; background-size:cover; background-position:center;
    margin-bottom:30px; box-shadow:0 30px 60px rgba(0,0,0,0.4);
  }
  .product-gallery-grid{
    display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; margin-top:36px;
  }
  .product-gallery-grid .thumb{
    height:150px; background-size:cover; background-position:center; border-radius:6px;
    filter:grayscale(0.1); transition:filter .3s ease, transform .3s ease;
  }
  .product-gallery-grid .thumb:hover{filter:grayscale(0); transform:scale(1.03);}
  @media (max-width:760px){ .product-gallery-grid{grid-template-columns:repeat(2, 1fr);} }
  .service-detail-main p{
    font-family:'Poppins'; font-size:15px; color:var(--gray); line-height:1.85; margin-bottom:20px;
  }
  .service-detail-main h3{
    font-family:'Jost'; font-size:22px; color:var(--white); margin:38px 0 16px; font-weight:600;
  }
  .service-sidebar{
    background:var(--ink2); border:1px solid rgba(255,255,255,0.08); padding:6px;
  }
  .service-sidebar h4{
    font-family:'Poppins'; font-size:12px; letter-spacing:0.12em; text-transform:uppercase;
    color:var(--white); padding:18px 20px 12px; border-bottom:2px solid var(--coral); margin-bottom:6px;
  }
  .service-sidebar a{
    display:flex; justify-content:space-between; align-items:center;
    font-family:'Poppins'; font-size:13px; letter-spacing:0.04em; text-transform:uppercase;
    color:var(--gray); padding:14px 20px; border-bottom:1px solid rgba(255,255,255,0.06); transition:all .2s;
  }
  .service-sidebar a:last-child{border-bottom:none;}
  .service-sidebar a:hover, .service-sidebar a.active{ background:var(--ink3); color:var(--white); padding-left:26px;}
  .service-detail-cta{
    margin-top:20px; padding:26px; background:var(--ink2); border-left:2px solid var(--coral);
  }
  .service-detail-cta p{ color:var(--gray); font-size:13px; margin-bottom:14px; }

  /* ---------- PRODUCT CATEGORY CARDS ---------- */
  .product-cat-grid{
    display:grid; grid-template-columns:repeat(4, 1fr); gap:1px; background:rgba(255,255,255,0.08);
  }
  .product-cat-card{
    display:block; background:var(--ink2); overflow:hidden; transition:background .3s;
  }
  .product-cat-card:hover{background:var(--ink3);}
  .product-cat-card .thumb{
    height:170px; background-size:cover; background-position:center; filter:grayscale(0.15);
  }
  .product-cat-card .body{padding:22px 22px 26px;}
  .product-cat-card h3{font-family:'Jost'; font-size:17px; color:var(--white); margin-bottom:8px; font-weight:600; text-transform:uppercase;}
  .product-cat-card p{font-family:'Poppins'; font-size:12px; color:var(--gray); line-height:1.6;}
  .product-cat-card .native-name{color:var(--coral); font-size:11px; font-family:'Poppins'; margin-bottom:4px; display:block;}

  /* ---------- PRODUCTS ---------- */
  .products-grid{
    display:grid; grid-template-columns:1fr 1fr; gap:1px; background:rgba(255,255,255,0.08);
  }
  .product-panel{
    position:relative; min-height:420px; display:flex; align-items:flex-end; overflow:hidden;
  }
  .product-panel::after{
    content:''; position:absolute; inset:0; background:linear-gradient(0deg, rgba(10,10,16,0.9), rgba(10,10,16,0.25));
  }
  .product-panel.pp1{background:radial-gradient(circle at 40% 30%, #3a3a3a, #0D0D0D 70%);}
  .product-panel.pp2{background:radial-gradient(circle at 60% 30%, #333333, #0D0D0D 70%);}
  .product-content{position:relative; z-index:2; padding:36px;}
  .product-content h3{font-size:30px; color:var(--white); margin-bottom:12px;}
  .product-content p{font-family:'Poppins'; font-size:14px; color:rgba(255,255,255,0.7); max-width:340px; margin-bottom:16px;}
  .product-badge{
    display:inline-block; font-family:'Poppins'; font-size:11px; color:var(--coral);
    border:1px solid var(--coral); padding:6px 12px; letter-spacing:0.08em;
  }

  /* ---------- ABOUT ---------- */
  .about-grid{display:grid; grid-template-columns:1fr 1fr; gap:70px; align-items:center;}
  .about-visual{
    aspect-ratio:4/5; background:radial-gradient(circle at 50% 30%, #383838, #0D0D0D 75%);
    position:relative;
  }
  .about p{font-family:'Poppins'; font-size:15px; color:var(--gray); margin-bottom:18px; max-width:480px; line-height:1.8;}
  .placeholder-note{
    font-family:'Poppins'; font-size:11px; color:var(--coral); border-left:2px solid var(--coral);
    padding-left:12px; margin-top:22px; letter-spacing:0.03em;
  }
  .about-stats{display:flex; gap:36px; margin-top:32px; flex-wrap:wrap;}
  .stat b{font-family:'Jost'; font-size:32px; display:block; color:var(--white);}
  .stat span{font-family:'Poppins'; font-size:11px; color:var(--gray); text-transform:uppercase; letter-spacing:0.05em;}

  /* ---------- PARTNERS / CERT GRID (style like reference logo grid) ---------- */
  .partners{background:var(--ink2); padding:80px 0;}
  .partner-grid{
    display:grid; grid-template-columns:repeat(4, 1fr); gap:1px; background:rgba(255,255,255,0.06);
  }
  .partner-box{
    background:var(--ink2); height:130px; display:flex; align-items:center; justify-content:center;
    font-family:'Poppins'; font-size:11px; color:var(--gray); letter-spacing:0.08em; text-transform:uppercase;
    text-align:center; padding:14px;
  }
  .cert-grid{
    display:grid; grid-template-columns:repeat(4, 1fr); gap:24px;
  }
  .cert-card{
    background:var(--white); border-radius:8px; overflow:hidden; box-shadow:0 20px 40px rgba(0,0,0,0.35);
    transition:transform .3s ease;
  }
  .cert-card:hover{transform:translateY(-6px);}
  .cert-card img{width:100%; display:block;}
  .cert-card p{
    font-family:'Poppins'; font-size:12px; color:var(--ink); text-align:center;
    padding:12px 10px; letter-spacing:0.02em; background:var(--white);
  }
  @media (max-width:860px){ .cert-grid{grid-template-columns:repeat(2, 1fr);} }

  /* ---------- BLOG ---------- */
  .blog-grid{
    display:grid; grid-template-columns:repeat(3, 1fr); gap:24px;
  }
  .blog-card{background:var(--ink2); border:1px solid rgba(255,255,255,0.08); overflow:hidden;}
  .blog-card .thumb{height:190px; background-size:cover; background-position:center;}
  .blog-card .body{padding:24px;}
  .blog-card .date{font-family:'Poppins'; font-size:11px; color:var(--gray); letter-spacing:0.05em; margin-bottom:10px; display:block;}
  .blog-card h3{font-size:19px; color:var(--white); margin-bottom:10px;}
  .blog-card p{font-family:'Poppins'; font-size:13px; color:var(--gray); line-height:1.7; margin-bottom:18px;}
  .blog-card .more{
    display:inline-block; font-family:'Poppins'; font-size:11px; letter-spacing:0.1em; text-transform:uppercase;
    color:var(--white); border:1px solid var(--coral); padding:9px 16px;
    transition:background .35s cubic-bezier(.4,0,.2,1), transform .35s cubic-bezier(.4,0,.2,1);
  }
  .blog-card .more:hover{background:var(--coral); transform:translateX(4px);}

  /* ---------- CONTACT ---------- */
  .contact-grid{display:grid; grid-template-columns:1fr 1fr; gap:70px;}
  .contact-list{list-style:none; margin-top:30px;}
  .contact-list li{
    display:flex; gap:18px; padding:16px 0; border-bottom:1px solid rgba(255,255,255,0.1);
    font-family:'Poppins'; font-size:14px; color:var(--gray);
  }
  .contact-list b{color:var(--white); width:100px; flex-shrink:0; font-size:11px; text-transform:uppercase; letter-spacing:0.08em;}
  .form-box{background:var(--ink2); padding:40px; border:1px solid rgba(255,255,255,0.08);}
  .form-row{margin-bottom:18px;}
  .form-row label{
    display:block; font-family:'Poppins'; font-size:11px; text-transform:uppercase; letter-spacing:0.08em;
    color:var(--gray); margin-bottom:8px;
  }
  .form-row input, .form-row textarea{
    width:100%; background:transparent; border:1px solid rgba(255,255,255,0.2); color:var(--white);
    padding:12px 14px; font-family:'Poppins'; font-size:14px;
  }
  .form-row input:focus, .form-row textarea:focus{outline:none; border-color:var(--coral);}
  .form-row textarea{min-height:90px; resize:vertical;}
  .submit-btn{
    font-family:'Poppins'; font-size:12px; letter-spacing:0.1em; text-transform:uppercase; color:var(--white);
    border:1px solid var(--coral); background:none; padding:14px 26px;
    transition:background .35s cubic-bezier(.4,0,.2,1), transform .35s cubic-bezier(.4,0,.2,1);
  }
  .submit-btn:hover{background:var(--coral); transform:translateX(4px);}
  .submit-btn:disabled{opacity:0.5; pointer-events:none;}
  .form-status{
    font-family:'Poppins'; font-size:13px; margin-top:14px; min-height:18px;
    opacity:0; transform:translateY(-4px); transition:opacity .3s ease, transform .3s ease;
  }
  .form-status.ok{opacity:1; transform:translateY(0); color:#7bd88f;}
  .form-status.err{opacity:1; transform:translateY(0); color:#e8746b;}
  .map-frame{
    border:1px solid rgba(255,255,255,0.1); filter:grayscale(0.3) invert(0.92) contrast(0.9);
    max-width:1300px; margin:0 auto;
  }

  /* ---------- FOOTER ---------- */
  footer{background:#0F0F17; padding:60px 0 28px;}
  .footer-grid{display:flex; justify-content:space-between; flex-wrap:wrap; gap:30px; margin-bottom:40px;}
  .footer-col h4{font-family:'Poppins'; font-size:11px; text-transform:uppercase; letter-spacing:0.1em; color:var(--white); margin-bottom:16px;}
  .footer-col a{display:block; font-family:'Poppins'; font-size:13px; color:var(--gray); margin-bottom:10px;}
  .footer-col a:hover{color:var(--coral);}
  .footer-bottom{
    border-top:1px solid rgba(255,255,255,0.08); padding-top:22px; display:flex;
    justify-content:space-between; font-family:'Poppins'; font-size:11px; color:var(--gray); flex-wrap:wrap; gap:10px;
  }

  @media (max-width:860px){
    .wrap{padding:0 24px;}
    .topbar{padding:24px 28px;}
    .fullmenu{padding:0 24px;}
    .menu-social{right:24px;}
    .banner-content{padding:0 24px 34px;}
    .service-grid{grid-template-columns:1fr;}
    .products-grid{grid-template-columns:1fr;}
    .product-cat-grid{grid-template-columns:repeat(2,1fr);}
    .service-detail-grid{grid-template-columns:1fr;}
    .about-grid{grid-template-columns:1fr;}
    .contact-grid{grid-template-columns:1fr;}
    .partner-grid{grid-template-columns:repeat(2,1fr);}
    .blog-grid{grid-template-columns:1fr;}
    .social-rail{left:10px; bottom:10px; gap:6px;}
    .social-rail a{width:36px; height:36px; font-size:15px;}
    .social-rail a svg{width:15px; height:15px;}
    .scroll-hint{left:56px;}
    .logo-img{height:52px;}
    .topbar-right{gap:10px;}
    .lang-current{padding:7px 12px; font-size:12px;}
    .lang-options{min-width:100px;}
  }

  /* ---------- RTL (Arabic) ---------- */
  html[dir="rtl"] body{font-family:'Tajawal', sans-serif;}
  html[dir="rtl"] h1, html[dir="rtl"] h2, html[dir="rtl"] h3, html[dir="rtl"] .serif{
    font-family:'Tajawal', sans-serif; text-transform:none; letter-spacing:0;
  }
  html[dir="rtl"] .social-rail{left:auto; right:14px;}
  html[dir="rtl"] .hero-dots{right:auto; left:36px;}
  html[dir="rtl"] .lang-options{right:auto; left:0;}
  html[dir="rtl"] .scroll-hint{left:auto; right:76px;}
  html[dir="rtl"] .scroll-hint .line::after{left:auto; right:-30px;}
  html[dir="rtl"] .service-card .more:hover,
  html[dir="rtl"] .blog-card .more:hover,
  html[dir="rtl"] .more:hover,
  html[dir="rtl"] .submit-btn:hover{transform:translateX(-4px);}
  html[dir="rtl"] .menu-social{direction:ltr;}
  @media (max-width:760px){
    html[dir="rtl"] .social-rail{left:auto; right:10px;}
    html[dir="rtl"] .scroll-hint{left:auto; right:56px;}
  }
"""

def nav_item(label, href, current, key):
    active = " active" if current == key else ""
    return f'<a href="{href}" class="menu-item{active}">{label}</a>'

NAV_LABELS = {
    "en": {"home":"Home","corporate":"Corporate","about":"About Us","certificates":"Certificates",
           "services":"Services","demir":"Iron &amp; Steel Products","paslanmaz":"Stainless Steel Products",
           "blog":"Blog","contact":"Contact"},
    "tr": {"home":"Anasayfa","corporate":"Kurumsal","about":"Hakk\u0131m\u0131zda","certificates":"Sertifikalar",
           "services":"Hizmetler","demir":"Demir \u00c7elik \u00dcr\u00fcnler","paslanmaz":"Paslanmaz \u00dcr\u00fcnler",
           "blog":"Blog","contact":"\u0130leti\u015fim"},
    "fr": {"home":"Accueil","corporate":"Entreprise","about":"\u00c0 propos","certificates":"Certificats",
           "services":"Services","demir":"Produits Fer et Acier","paslanmaz":"Produits Inox",
           "blog":"Blog","contact":"Contact"},
    "ar": {"home":"\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629","corporate":"\u0627\u0644\u0634\u0631\u0643\u0629","about":"\u0645\u0646 \u0646\u062d\u0646","certificates":"\u0627\u0644\u0634\u0647\u0627\u062f\u0627\u062a",
           "services":"\u0627\u0644\u062e\u062f\u0645\u0627\u062a","demir":"\u0645\u0646\u062a\u062c\u0627\u062a \u0627\u0644\u062d\u062f\u064a\u062f \u0648\u0627\u0644\u0635\u0644\u0628","paslanmaz":"\u0645\u0646\u062a\u062c\u0627\u062a \u0627\u0644\u0633\u062a\u0627\u0646\u0644\u0633 \u0633\u062a\u064a\u0644",
           "blog":"\u0627\u0644\u0645\u062f\u0648\u0646\u0629","contact":"\u0627\u062a\u0635\u0644 \u0628\u0646\u0627"},
}

LANGS = ["en", "tr", "fr", "ar"]
LANG_FOLDER = {"tr": "", "en": "en/", "fr": "fr/", "ar": "ar/"}
LANG_CODE = {"en": "EN", "tr": "TR", "fr": "FR", "ar": "AR"}
LANG_NAME = {"en": "English", "tr": "T\u00fcrk\u00e7e", "fr": "Fran\u00e7ais", "ar": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"}

def lang_url(from_lang, to_lang, slug):
    from_root = LANG_FOLDER[from_lang] == ""
    to_root = LANG_FOLDER[to_lang] == ""
    if from_root:
        return f"{LANG_FOLDER[to_lang]}{slug}.html"
    if to_root:
        return f"../{slug}.html"
    return f"../{LANG_FOLDER[to_lang]}{slug}.html"

SITE_URL = "https://norapaslanmazcelik.com"

def hreflang_tags(slug):
    tags = []
    for code in LANGS:
        url = f"{SITE_URL}/{LANG_FOLDER[code]}{slug}.html"
        tags.append(f'<link rel="alternate" hreflang="{code}" href="{url}">')
    tags.append(f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/{slug}.html">')
    return "\n".join(tags)

def lang_switcher_links(lang, slug):
    return "\n".join([
        f'<a class="lang-switch" href="{lang_url(lang, code, slug)}">{LANG_CODE[code]}</a>'
        for code in LANGS if code != lang
    ])

def build_chrome(current, lang="en", slug="index"):
    L = NAV_LABELS[lang]
    corp_active = "active" if current in ("about", "certificates") else ""
    cursor = '<div id="cursor"></div><canvas id="dustCanvas"></canvas>'
    social = """
<div class="social-rail">
  <a class="phone" href="tel:02166215541" aria-label="Call us">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
  </a>
  <a class="linkedin" href="https://www.linkedin.com/in/nora-global-steel-25b6a3420" target="_blank" rel="noopener" aria-label="LinkedIn">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="#fff"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.38-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45z"/></svg>
  </a>
  <a class="whatsapp" href="https://wa.me/905550532457" target="_blank" rel="noopener" aria-label="WhatsApp">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="#fff"><path d="M17.47 14.38c-.29-.15-1.7-.84-1.97-.93-.26-.1-.46-.15-.65.14-.2.3-.75.94-.92 1.13-.17.2-.34.22-.63.08-.29-.15-1.22-.45-2.33-1.44-.86-.77-1.44-1.72-1.6-2.02-.17-.29-.02-.45.13-.6.13-.13.29-.34.44-.5.15-.18.2-.3.29-.5.1-.2.05-.37-.02-.51-.08-.15-.65-1.58-.9-2.16-.24-.58-.48-.5-.65-.5-.17 0-.37-.02-.56-.02-.2 0-.51.07-.78.37s-1.03 1-1.03 2.45 1.05 2.85 1.2 3.05c.15.2 2.06 3.15 5 4.42.7.3 1.24.48 1.67.61.7.22 1.34.19 1.84.12.56-.08 1.7-.7 1.95-1.36.24-.67.24-1.24.17-1.36-.07-.12-.26-.2-.55-.35z"/><path d="M12.04 2C6.55 2 2.1 6.44 2.1 11.94c0 1.87.51 3.62 1.4 5.12L2 22l5.08-1.44a9.9 9.9 0 0 0 4.96 1.33h.01c5.49 0 9.94-4.44 9.94-9.94S17.53 2 12.04 2zm0 18.16h-.01a8.2 8.2 0 0 1-4.18-1.15l-.3-.18-3.02.85.85-2.94-.2-.31a8.16 8.16 0 0 1-1.26-4.4c0-4.51 3.67-8.18 8.19-8.18a8.13 8.13 0 0 1 5.79 2.4 8.13 8.13 0 0 1 2.39 5.78c0 4.52-3.68 8.13-8.25 8.13z"/></svg>
  </a>
  <a class="instagram" href="https://instagram.com/nora_steel_global" target="_blank" rel="noopener" aria-label="Instagram">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#fff" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1"/></svg>
  </a>
</div>
"""
    topbar = f"""
<div class="topbar">
  <a href="index.html" class="logo">
    <img class="logo-img" src="{NORA_LOGO_PATH}" alt="Nora Paslanmaz ve Demir Celik">
  </a>
  <div class="topbar-right">
    <div class="lang-dropdown" id="langDropdown">
      <button class="lang-current" id="langCurrentBtn" type="button" aria-haspopup="true" aria-expanded="false">{LANG_CODE[lang]}</button>
      <div class="lang-options" id="langOptions">
        {lang_switcher_links(lang, slug)}
      </div>
    </div>
    <button class="menu-btn" id="menuBtn"><span class="bar"></span></button>
  </div>
</div>
"""
    fullmenu = f"""
<div class="fullmenu" id="fullMenu">
  <button class="menu-close" id="menuClose" aria-label="Close menu">
    <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><path d="M4 4 L20 20 M20 4 L4 20"/></svg>
  </button>
  <div class="menu-inner">
  <ul class="menu-list">
    <li>{nav_item(L["home"], "index.html", current, "home")}</li>
    <li>
      <div class="menu-item {corp_active}" id="corporateToggle">{L["corporate"]} <span class="chev">&#8964;</span></div>
      <ul class="submenu" id="corporateSub">
        <li><a href="about.html" class="{'active' if current=='about' else ''}">{L["about"]}</a></li>
        <li><a href="certificates.html" class="{'active' if current=='certificates' else ''}">{L["certificates"]}</a></li>
      </ul>
    </li>
    <li>{nav_item(L["services"], "services.html", current, "services")}</li>
    <li>{nav_item(L["demir"], "demir-celik-urunler.html", current, "demir")}</li>
    <li>{nav_item(L["paslanmaz"], "paslanmaz-urunler.html", current, "paslanmaz")}</li>
    <li>{nav_item(L["blog"], "blog.html", current, "blog")}</li>
    <li>{nav_item(L["contact"], "contact.html", current, "contact")}</li>
  </ul>
  </div>
  <div class="menu-social">
    <a href="#">Facebook</a>
    <a href="#">Instagram</a>
    <a href="#">Linkedin</a>
  </div>
</div>
"""
    return cursor + social + topbar + fullmenu

FOOTER_LABELS = {
    "en": {"corporate":"Corporate","company":"Company","contact":"Contact","language":"Language",
           "certificates":"Certificates","references":"References","blog":"Blog",
           "copyright":"&copy; 2026 Nora Paslanmaz ve Demir Celik"},
    "tr": {"corporate":"Kurumsal","company":"\u015eirket","contact":"\u0130leti\u015fim","language":"Dil",
           "certificates":"Sertifikalar","references":"Referanslar","blog":"Blog",
           "copyright":"&copy; 2026 Nora Paslanmaz ve Demir \u00c7elik"},
    "fr": {"corporate":"Entreprise","company":"Soci\u00e9t\u00e9","contact":"Contact","language":"Langue",
           "certificates":"Certificats","references":"R\u00e9f\u00e9rences","blog":"Blog",
           "copyright":"&copy; 2026 Nora Paslanmaz ve Demir Celik"},
    "ar": {"corporate":"الشركة","company":"الأقسام","contact":"اتصل بنا","language":"اللغة",
           "certificates":"الشهادات","references":"المراجع","blog":"المدونة",
           "copyright":"&copy; 2026 نورا للصلب والستانلس"},
}

def footer_html(lang="en", slug="index"):
    F = FOOTER_LABELS[lang]
    N = NAV_LABELS[lang]
    lang_links = "\n        ".join([
        f'<a href="{lang_url(lang, code, slug)}">{LANG_NAME[code]}</a>'
        for code in LANGS if code != lang
    ])
    return f"""
<footer>
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>Nora Paslanmaz ve Celik</h4>
        <a href="about.html">{F["corporate"]}</a>
        <a href="services.html">{N["services"]}</a>
        <a href="demir-celik-urunler.html">{N["demir"]}</a>
        <a href="paslanmaz-urunler.html">{N["paslanmaz"]}</a>
      </div>
      <div class="footer-col">
        <h4>{F["company"]}</h4>
        <a href="certificates.html">{F["certificates"]}</a>
        <a href="certificates.html">{F["references"]}</a>
        <a href="blog.html">{F["blog"]}</a>
      </div>
      <div class="footer-col">
        <h4>{F["contact"]}</h4>
        <a href="tel:02166215541">0216 621 55 41</a>
        <a href="mailto:info@norapaslanmazglobal.com">info@norapaslanmazglobal.com</a>
      </div>
      <div class="footer-col">
        <h4>{F["language"]}</h4>
        {lang_links}
      </div>
    </div>
    <div class="footer-bottom">
      <span>{F["copyright"]}</span>
      <span>norapaslanmazcelik.com</span>
    </div>
  </div>
</footer>
"""

SHARED_SCRIPT_BASE = """
<script>
  // Elegant page-to-page transition: intercept same-site link clicks, play a
  // short fade+lift exit animation, then navigate. Entrance animation on the
  // next page is handled purely by CSS (see pageEnter keyframes), so this
  // still degrades gracefully if JS is blocked, links just work instantly.
  (function(){
    document.addEventListener('click', function(e){
      if (e.defaultPrevented || e.button !== 0) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      const a = e.target.closest('a[href]');
      if (!a) return;
      const href = a.getAttribute('href');
      if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) return;
      if (a.target === '_blank' || a.hasAttribute('download')) return;
      if (/^https?:\\/\\//i.test(href) && href.indexOf(location.hostname) === -1) return;
      e.preventDefault();
      document.body.classList.add('page-leaving');
      setTimeout(()=>{ window.location.href = href; }, 300);
    });
    // Pages restored from bfcache (browser back/forward) skip the JS re-run,
    // so make sure they're never left stuck mid-exit-animation.
    window.addEventListener('pageshow', function(){
      document.body.classList.remove('page-leaving');
    });
  })();

  // Language dropdown: click the current-language pill to reveal the other
  // languages; closes on outside click or after picking one.
  (function(){
    const dropdown = document.getElementById('langDropdown');
    const btn = document.getElementById('langCurrentBtn');
    if (!dropdown || !btn) return;
    btn.addEventListener('click', function(e){
      e.stopPropagation();
      const isOpen = dropdown.classList.toggle('open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    document.addEventListener('click', function(e){
      if (!dropdown.contains(e.target)){
        dropdown.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  })();

  // Contact form -> Web3Forms, submitted via fetch so the page never
  // reloads; shows an inline status message instead.
  document.querySelectorAll('.ajax-form').forEach(function(form){
    const status = form.querySelector('.form-status');
    const btn = form.querySelector('button[type="submit"]');
    form.addEventListener('submit', function(e){
      e.preventDefault();
      if (btn){ btn.disabled = true; }
      if (status){ status.textContent = ''; status.className = 'form-status'; }
      fetch('https://api.web3forms.com/submit', {
        method: 'POST',
        headers: { 'Accept': 'application/json' },
        body: new FormData(form)
      })
      .then(r => r.json())
      .then(data => {
        if (data.success){
          if (status){ status.textContent = form.dataset.success; status.classList.add('ok'); }
          form.reset();
        } else {
          if (status){ status.textContent = form.dataset.error; status.classList.add('err'); }
        }
      })
      .catch(() => {
        if (status){ status.textContent = form.dataset.error; status.classList.add('err'); }
      })
      .finally(() => { if (btn){ btn.disabled = false; } });
    });
  });

  // Custom round cursor
  const cursor = document.getElementById('cursor');
  let mx=0, my=0, cx=0, cy=0;
  document.addEventListener('mousemove', e=>{
    mx=e.clientX; my=e.clientY;
    if (!cursor.classList.contains('visible')) { cx = mx; cy = my; cursor.classList.add('visible'); }
  });
  function animCursor(){
    cx += (mx-cx)*0.18; cy += (my-cy)*0.18;
    cursor.style.left = cx+'px'; cursor.style.top = cy+'px';
    requestAnimationFrame(animCursor);
  }
  animCursor();
  document.querySelectorAll('a, button, .menu-item').forEach(el=>{
    el.addEventListener('mouseenter', ()=>cursor.classList.add('grow'));
    el.addEventListener('mouseleave', ()=>cursor.classList.remove('grow'));
  });

  // Fullscreen menu toggle
  const menuBtn = document.getElementById('menuBtn');
  const fullMenu = document.getElementById('fullMenu');
  let savedScrollY = 0;
  function openMenu(){
    savedScrollY = window.scrollY;
    fullMenu.classList.add('open');
    menuBtn.classList.add('open');
    menuBtn.style.visibility = 'hidden';
    document.body.classList.add('menu-open');
    document.body.style.position = 'fixed';
    document.body.style.top = -savedScrollY + 'px';
    document.body.style.left = '0';
    document.body.style.right = '0';
  }
  function closeMenu(){
    fullMenu.classList.remove('open');
    menuBtn.classList.remove('open');
    menuBtn.style.visibility = 'visible';
    document.body.classList.remove('menu-open');
    document.body.style.position = '';
    document.body.style.top = '';
    document.body.style.left = '';
    document.body.style.right = '';
    window.scrollTo(0, savedScrollY);
  }
  menuBtn.addEventListener('click', ()=>{
    if (fullMenu.classList.contains('open')) closeMenu(); else openMenu();
  });
  document.getElementById('menuClose').addEventListener('click', closeMenu);

  // Corporate submenu toggle
  const corpToggle = document.getElementById('corporateToggle');
  const corpSub = document.getElementById('corporateSub');
  corpToggle.addEventListener('click', ()=>{
    corpToggle.classList.toggle('active');
    corpSub.classList.toggle('open');
  });

  // Smooth scroll-reveal animations across the site
  const revealEls = document.querySelectorAll('.reveal, .reveal-stagger');
  const revealObserver = new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
      if (entry.isIntersecting){
        entry.target.classList.add('in');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
  revealEls.forEach(el=> revealObserver.observe(el));

  // Ambient dust particles - subtle floating motes across the whole site,
  // drifting upward with gentle drift, giving the page a sense of life
  (function(){
    const canvas = document.getElementById('dustCanvas');
    const ctx = canvas.getContext('2d');
    let W, H, particles = [];
    const COUNT = 46;

    function resize(){
      W = canvas.width = window.innerWidth;
      H = canvas.height = window.innerHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    function makeParticle(){
      return {
        x: Math.random() * W,
        y: Math.random() * H,
        r: 0.6 + Math.random() * 1.8,
        speedY: 0.08 + Math.random() * 0.22,
        driftX: (Math.random() - 0.5) * 0.25,
        alpha: 0.15 + Math.random() * 0.35,
        twinkle: Math.random() * Math.PI * 2
      };
    }
    for (let i = 0; i < COUNT; i++) particles.push(makeParticle());

    function tick(){
      ctx.clearRect(0, 0, W, H);
      particles.forEach(p=>{
        p.y -= p.speedY;
        p.x += p.driftX;
        p.twinkle += 0.02;
        if (p.y < -10){ p.y = H + 10; p.x = Math.random() * W; }
        if (p.x < -10) p.x = W + 10;
        if (p.x > W + 10) p.x = -10;
        const flicker = (Math.sin(p.twinkle) + 1) / 2;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255,255,255,${(p.alpha * (0.5 + flicker * 0.5)).toFixed(3)})`;
        ctx.fill();
      });
      requestAnimationFrame(tick);
    }
    tick();
  })();

  // Cursor-reactive tilt on cards - a gentle 3D tilt following the pointer,
  // applied to every card-style element across the site (services, products, blog)
  (function(){
    const tiltEls = document.querySelectorAll('.service-card, .product-cat-card, .blog-card, .partner-box');
    tiltEls.forEach(el=>{
      el.style.transition = 'transform .25s ease, box-shadow .25s ease';
      el.style.willChange = 'transform';
      el.addEventListener('mousemove', (e)=>{
        const rect = el.getBoundingClientRect();
        const px = (e.clientX - rect.left) / rect.width - 0.5;
        const py = (e.clientY - rect.top) / rect.height - 0.5;
        const rotX = (py * -6).toFixed(2);
        const rotY = (px * 8).toFixed(2);
        el.style.transform = `perspective(700px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale(1.02) translateZ(0)`;
        el.style.boxShadow = `${(-px*18).toFixed(0)}px ${(12-py*10).toFixed(0)}px 34px rgba(0,0,0,0.45)`;
      });
      el.addEventListener('mouseleave', ()=>{
        el.style.transform = 'perspective(700px) rotateX(0deg) rotateY(0deg) scale(1)';
        el.style.boxShadow = 'none';
      });
    });
  })();
"""

def hero_script(slides):
    slides_js = ",\n    ".join([
        f"{{ eyebrow: '{ey}', title: '{ti}', img: '{IMG_B64[img]}', link: '{link}' }}"
        for ey, ti, img, link in slides
    ])
    return f"""
  // Hero - smooth horizontal filmstrip slide. All slides sit in a row inside
  // .hero-track; advancing moves the whole track left/right by exactly one
  // slide's pitch (width + gap) using a single CSS transform transition, so
  // the motion reads as one continuous, physical slide, no shrink/dip, no
  // mid-animation content swap. The active slide also crossfades into focus
  // (blur/scale) over the same duration, driven purely by the .active class.
  const heroSlidesData = [
    {slides_js}
  ];
  const n = heroSlidesData.length;
  const heroSpacer = document.getElementById('heroSpacer');
  const heroFixed = document.getElementById('heroFixed');
  const heroTrack = document.getElementById('heroTrack');
  const labelEyebrow = document.getElementById('labelEyebrow');
  const labelTitle = document.getElementById('labelTitle');

  heroSpacer.style.height = '100vh';

  // Build the slide elements once
  const slideEls = heroSlidesData.map((s, i) => {{
    const a = document.createElement('a');
    a.className = 'hero-slide';
    a.style.backgroundImage = `url(${{s.img}})`;
    a.href = s.link;
    a.setAttribute('aria-label', s.title);
    heroTrack.appendChild(a);
    return a;
  }});

  let idx = 0;
  let heroActive = true;
  let animBusy = false;
  let metrics = {{ slideW: 0, gap: 0, pitch: 0 }};

  function computeMetrics(){{
    const vw = window.innerWidth;
    const mobile = vw <= 760;
    const slideW = mobile ? vw * 0.94 : Math.min(1240, Math.max(760, vw * 0.66));
    const gap = mobile ? vw * 0.025 : vw * 0.015;
    return {{ slideW, gap, pitch: slideW + gap }};
  }}

  function layout(instant){{
    metrics = computeMetrics();
    const sidePad = Math.max(0, (window.innerWidth - metrics.slideW) / 2);
    heroTrack.style.paddingLeft = sidePad + 'px';
    heroTrack.style.paddingRight = sidePad + 'px';
    slideEls.forEach((el, i) => {{
      el.style.width = metrics.slideW + 'px';
      el.style.marginRight = (i < n - 1 ? metrics.gap : 0) + 'px';
    }});
    if (instant) heroTrack.style.transition = 'none';
    heroTrack.style.transform = `translateX(${{-idx * metrics.pitch}}px)`;
    if (instant){{
      // force reflow so the transition:none actually applies before we restore it
      void heroTrack.offsetHeight;
      heroTrack.style.transition = '';
    }}
  }}

  function paintState(){{
    slideEls.forEach((el, i) => el.classList.toggle('active', i === idx));
    labelEyebrow.innerHTML = heroSlidesData[idx].eyebrow;
    labelTitle.innerHTML = heroSlidesData[idx].title;
  }}

  layout(true);
  paintState();

  window.addEventListener('resize', () => layout(true));

  function lockScroll(){{ document.documentElement.style.overflow = 'hidden'; }}
  function unlockScroll(){{ document.documentElement.style.overflow = ''; }}
  lockScroll();

  function enterHero(atEnd){{
    heroActive = true;
    idx = atEnd ? n - 1 : 0;
    layout(true);
    paintState();
    heroFixed.classList.remove('exited');
    lockScroll();
  }}

  function exitHero(forward){{
    heroActive = false;
    heroFixed.classList.add('exited');
    unlockScroll();
    const rect = heroSpacer.getBoundingClientRect();
    const targetY = forward
      ? window.scrollY + rect.bottom + 2
      : window.scrollY + rect.top - 2;
    window.scrollTo(0, Math.max(targetY, 0));
  }}

  // One tick = one full slide, moved by a single continuous transform
  // transition. The active slide's focus crossfade runs on the same clock.
  function advance(newIdx){{
    idx = newIdx;
    animBusy = true;
    heroTrack.style.transform = `translateX(${{-idx * metrics.pitch}}px)`;
    paintState();
    setTimeout(()=>{{ animBusy = false; }}, 700);
  }}

  window.addEventListener('wheel', function(e){{
    if (document.getElementById('fullMenu').classList.contains('open')) return;

    if (!heroActive){{
      const rect = heroSpacer.getBoundingClientRect();
      const nearHeroFromBelow = e.deltaY < 0 && rect.bottom > 0 && rect.bottom <= window.innerHeight + 60;
      if (nearHeroFromBelow){{
        e.preventDefault();
        enterHero(true);
      }}
      return;
    }}

    e.preventDefault();
    if (animBusy) return;
    const dir = e.deltaY > 0 ? 1 : -1;

    if (dir === 1){{
      if (idx < n - 1) advance(idx + 1);
      else exitHero(true);
    }} else {{
      if (idx > 0) advance(idx - 1);
    }}
  }}, {{ passive: false }});

  let touchStartY = null;
  window.addEventListener('touchstart', function(e){{
    touchStartY = e.touches[0].clientY;
  }}, {{ passive: true }});
  window.addEventListener('touchend', function(e){{
    if (touchStartY === null) return;
    const dy = touchStartY - e.changedTouches[0].clientY;
    touchStartY = null;
    if (Math.abs(dy) < 40) return;
    if (!heroActive){{
      const rect = heroSpacer.getBoundingClientRect();
      if (dy < 0 && rect.bottom > 0 && rect.bottom <= window.innerHeight + 60) enterHero(true);
      return;
    }}
    if (animBusy) return;
    const dir = dy > 0 ? 1 : -1;
    if (dir === 1){{
      if (idx < n - 1) advance(idx + 1);
      else exitHero(true);
    }} else {{
      if (idx > 0) advance(idx - 1);
    }}
  }}, {{ passive: true }});
"""

HERO_SLIDES_EN = [
    ("Service / 01", "CNC Machining", "cnc", "services.html"),
    ("Service / 02", "Laser Cutting", "laser", "services.html"),
    ("Service / 03", "Plasma Cutting", "plasma", "services.html"),
    ("Service / 04", "Welded Fabrication", "welded_fab", "services.html"),
    ("Service / 05", "Cutting &amp; Bending", "cutbend", "services.html"),
    ("Products", "Pipes, Tubes &amp; Steel", "pipes", "demir-celik-urunler.html"),
]
HERO_SCRIPT = hero_script(HERO_SLIDES_EN)

SITE_URL = "https://norapaslanmazcelik.com"
WEB3FORMS_KEY = "PASTE_YOUR_WEB3FORMS_ACCESS_KEY_HERE"
NAP = {
    "name": "Nora Paslanmaz ve Demir Celik",
    "phone": "+90 216 621 55 41",
    "email": "info@norapaslanmazglobal.com",
    "street": "OSB Des Sanayi Sitesi 115 Sok. No:30, Yukari Dudullu",
    "city": "Umraniye / Istanbul",
    "country": "TR",
}

META_DESC = {
    "en": {
        "index": "Nora Paslanmaz ve Celik is an Istanbul-based manufacturer and supplier of iron, steel, and stainless steel products, offering supply, cutting, bending, welding, and CNC machining.",
        "services": "Six core services from Nora Paslanmaz ve Celik: iron and steel supply, cutting and bending, CNC machining, welded fabrication, plasma cutting, and laser cutting.",
        "iron-steel-supply": "Direct supply of iron and steel sheet, profile, pipe, rolled stock, and steel mesh from Nora Paslanmaz ve Celik, Istanbul, with cutting and bending on request.",
        "cutting-bending": "CNC press-brake cutting and bending of sheet metal in a range of thicknesses and tonnages, from Nora Paslanmaz ve Celik in Istanbul.",
        "cnc-machining": "CNC turning, milling, drilling, and grinding services from Nora Paslanmaz ve Celik, bringing parts to exact dimension and surface finish.",
        "welded-fabrication": "Structural and custom welded fabrication in stainless steel, iron, and aluminum, from single parts to full assemblies, by Nora Paslanmaz ve Celik.",
        "plasma-cutting": "High-speed plasma cutting for steel and non-ferrous metal up to 25mm, fast and low-waste, from Nora Paslanmaz ve Celik in Istanbul.",
        "laser-cutting": "Precision laser cutting on stainless steel, iron, and aluminum sheet, clean edges and fast turnaround, from Nora Paslanmaz ve Celik.",
        "demir-celik-urunler": "Browse Nora's iron and steel product categories: sheet, profile, pipe, rolled stock, and steel mesh, supplied direct from Istanbul.",
        "paslanmaz-urunler": "Browse Nora's stainless steel product categories: sheet, profile, pipe, round bar, and fittings, supplied direct from Istanbul.",
        "about": "Nora Paslanmaz ve Celik is an experienced manufacturing partner for iron, steel, and stainless steel products, based in Istanbul, Turkey.",
        "certificates": "Certificates and industry references for Nora Paslanmaz ve Celik, an Istanbul-based iron, steel, and stainless steel manufacturer.",
        "blog": "News and technical articles from Nora Paslanmaz ve Celik on iron, steel, and stainless steel products.",
        "contact": "Get in touch with Nora Paslanmaz ve Celik for a quote on iron, steel, and stainless steel products and services in Istanbul.",
        "iron-steel-products-explained": "What are iron and steel products? A guide to sheet, profile, pipe, and rolled stock from Nora Paslanmaz ve Celik.",
        "stainless-steel-products-explained": "What is stainless steel and where does it offer an advantage? A guide from Nora Paslanmaz ve Celik.",
    },
    "tr": {
        "index": "Nora Paslanmaz ve Celik, Istanbul merkezli demir, celik ve paslanmaz celik uretici ve tedarikcisidir. Tedarik, kesim, bukum, kaynak ve talasli imalat hizmetleri sunar.",
        "services": "Nora Paslanmaz ve Celik'ten alti temel hizmet: demir celik urun, kesim bukum, talasli imalat, kaynakli imalat, plazma kesim ve lazer kesim.",
        "iron-steel-supply": "Nora Paslanmaz ve Celik'ten dogrudan demir celik urun tedariki, sac, profil, boru, hadde urunleri ve celik hasir, talep uzerine kesim ve bukum ile.",
        "cutting-bending": "Farkli kalinlik ve tonajlarda CNC pres bukum ile sac kesim ve bukum hizmeti, Istanbul merkezli Nora Paslanmaz ve Celik'ten.",
        "cnc-machining": "Nora Paslanmaz ve Celik'ten CNC tornalama, frezeleme, delme ve taslama hizmetleri, parcalari tam olcusune getiriyoruz.",
        "welded-fabrication": "Paslanmaz, demir ve aluminyum uzerinde yapisal ve ozel kaynakli imalat, Nora Paslanmaz ve Celik guvencesiyle.",
        "plasma-cutting": "25 mm'ye kadar celik ve demir disi malzemelerde hizli, dusuk fireli plazma kesim, Istanbul merkezli Nora Paslanmaz ve Celik'ten.",
        "laser-cutting": "Paslanmaz, demir ve aluminyum sac uzerinde hassas lazer kesim, temiz kenar ve hizli teslimat, Nora Paslanmaz ve Celik'ten.",
        "demir-celik-urunler": "Nora'nin demir celik urun kategorilerini inceleyin: sac, profil, boru, hadde urunleri ve celik hasir, Istanbul'dan dogrudan tedarik.",
        "paslanmaz-urunler": "Nora'nin paslanmaz celik urun kategorilerini inceleyin: sac, profil, boru, yuvarlak cubuk ve fittings, Istanbul'dan dogrudan tedarik.",
        "about": "Nora Paslanmaz ve Celik, Istanbul merkezli, demir, celik ve paslanmaz celik urunlerinde deneyimli bir uretim ortagidir.",
        "certificates": "Nora Paslanmaz ve Celik'in sertifikalari ve sektor referanslari, Istanbul merkezli demir celik ve paslanmaz celik ureticisi.",
        "blog": "Nora Paslanmaz ve Celik'ten demir, celik ve paslanmaz celik urunleri hakkinda haberler ve teknik yazilar.",
        "contact": "Istanbul'daki demir, celik ve paslanmaz celik urun ve hizmetleri icin Nora Paslanmaz ve Celik ile iletisime gecin.",
        "iron-steel-products-explained": "Demir celik urunleri nedir? Nora Paslanmaz ve Celik'ten sac, profil, boru ve hadde urunleri rehberi.",
        "stainless-steel-products-explained": "Paslanmaz celik nedir, nerede avantaj saglar? Nora Paslanmaz ve Celik'ten rehber.",
    },
    "fr": {
        "index": "Nora Paslanmaz ve Celik est un fabricant et fournisseur de fer, d'acier et d'acier inoxydable basé à Istanbul, proposant fourniture, découpe, pliage, soudure et usinage CNC.",
        "services": "Six métiers essentiels chez Nora Paslanmaz ve Celik : fourniture de fer et d'acier, découpe et pliage, usinage CNC, fabrication soudée, découpe plasma et découpe laser.",
        "iron-steel-supply": "Fourniture directe de tôle, profilé, tube, produits laminés et treillis d'acier par Nora Paslanmaz ve Celik, à Istanbul, avec découpe et pliage sur demande.",
        "cutting-bending": "Découpe et pliage sur presse CNC pour tôle, dans différentes épaisseurs et tonnages, par Nora Paslanmaz ve Celik à Istanbul.",
        "cnc-machining": "Services de tournage, fraisage, perçage et rectification CNC par Nora Paslanmaz ve Celik, pour des pièces aux dimensions et finitions exactes.",
        "welded-fabrication": "Fabrication soudée structurelle et sur mesure en inox, fer et aluminium, de la pièce unique à l'ensemble complet, par Nora Paslanmaz ve Celik.",
        "plasma-cutting": "Découpe plasma rapide, à faibles chutes, sur acier et métaux non ferreux jusqu'à 25 mm, par Nora Paslanmaz ve Celik à Istanbul.",
        "laser-cutting": "Découpe laser de précision sur tôle inox, fer et aluminium, bords nets et délais rapides, par Nora Paslanmaz ve Celik.",
        "demir-celik-urunler": "Découvrez les catégories de produits en fer et acier de Nora : tôle, profilé, tube, produits laminés et treillis d'acier, fournis depuis Istanbul.",
        "paslanmaz-urunler": "Découvrez les catégories de produits en acier inoxydable de Nora : tôle, profilé, tube, barre ronde et raccords, fournis depuis Istanbul.",
        "about": "Nora Paslanmaz ve Celik est un partenaire de fabrication expérimenté pour les produits en fer, acier et acier inoxydable, basé à Istanbul.",
        "certificates": "Certificats et références sectorielles de Nora Paslanmaz ve Celik, fabricant de fer, d'acier et d'acier inoxydable basé à Istanbul.",
        "blog": "Actualités et articles techniques de Nora Paslanmaz ve Celik sur les produits en fer, acier et acier inoxydable.",
        "contact": "Contactez Nora Paslanmaz ve Celik pour un devis sur les produits et services en fer, acier et acier inoxydable à Istanbul.",
        "iron-steel-products-explained": "Que sont les produits en fer et acier ? Un guide sur la tôle, les profilés, les tubes et les produits laminés, par Nora Paslanmaz ve Celik.",
        "stainless-steel-products-explained": "Qu'est-ce que l'acier inoxydable et où offre-t-il un avantage ? Un guide de Nora Paslanmaz ve Celik.",
    },
    "ar": {
        "index": "نورا للصلب والستانلس هي شركة مصنعة وموردة للحديد والصلب والستانلس ستيل مقرها إسطنبول، تقدم خدمات التوريد والقص والثني واللحام والتشغيل الآلي CNC.",
        "services": "ست خدمات أساسية من نورا: توريد الحديد والصلب، القص والثني، التشغيل الآلي CNC، التصنيع باللحام، القص بالبلازما، والقص بالليزر.",
        "iron-steel-supply": "توريد مباشر لصفائح وقطاعات وأنابيب ومنتجات درفلة وشباك صلب من نورا في إسطنبول، مع خدمات القص والثني عند الطلب.",
        "cutting-bending": "خدمة قص وثني الصفائح المعدنية بمكابس CNC بمختلف السماكات والأوزان، من نورا للصلب والستانلس في إسطنبول.",
        "cnc-machining": "خدمات الخراطة والتفريز والحفر والتجليخ بتقنية CNC من نورا، لتشكيل القطع بأبعاد ونهاية سطحية دقيقة.",
        "welded-fabrication": "تصنيع باللحام الإنشائي والمخصص للستانلس ستيل والحديد والألمنيوم، من قطعة واحدة إلى تجميع كامل، من نورا للصلب والستانلس.",
        "plasma-cutting": "قص بالبلازما عالي السرعة للصلب والمعادن غير الحديدية حتى 25 مم، سريع وبهدر منخفض، من نورا في إسطنبول.",
        "laser-cutting": "قص بالليزر عالي الدقة على صفائح الستانلس ستيل والحديد والألمنيوم، بحواف نظيفة وتسليم سريع، من نورا للصلب والستانلس.",
        "demir-celik-urunler": "تصفح فئات منتجات الحديد والصلب من نورا: صفائح، قطاعات، أنابيب، منتجات درفلة، وشباك صلب، توريد مباشر من إسطنبول.",
        "paslanmaz-urunler": "تصفح فئات منتجات الستانلس ستيل من نورا: صفائح، قطاعات، أنابيب، قضبان مستديرة، ووصلات، توريد مباشر من إسطنبول.",
        "about": "نورا للصلب والستانلس شريك تصنيع ذو خبرة في منتجات الحديد والصلب والستانلس ستيل، مقرها إسطنبول، تركيا.",
        "certificates": "الشهادات والمراجع الصناعية لشركة نورا للصلب والستانلس، الشركة المصنعة للحديد والصلب والستانلس ستيل في إسطنبول.",
        "blog": "أخبار ومقالات تقنية من نورا للصلب والستانلس حول منتجات الحديد والصلب والستانلس ستيل.",
        "contact": "تواصل مع نورا للصلب والستانلس للحصول على عرض سعر لمنتجات وخدمات الحديد والصلب والستانلس ستيل في إسطنبول.",
        "iron-steel-products-explained": "ما هي منتجات الحديد والصلب؟ دليل حول الصفائح والقطاعات والأنابيب ومنتجات الدرفلة من نورا للصلب والستانلس.",
        "stainless-steel-products-explained": "ما هو الستانلس ستيل وأين تكمن مزاياه؟ دليل من نورا للصلب والستانلس.",
    },
}

def schema_org(lang, slug, page_type="WebPage", svc=None):
    """Return a JSON-LD <script> block. Always includes the Organization
    (NAP data), plus a Service block on service detail pages."""
    import json
    org = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": NAP["name"],
        "url": SITE_URL,
        "telephone": NAP["phone"],
        "email": NAP["email"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": NAP["street"],
            "addressLocality": "Istanbul",
            "addressCountry": NAP["country"],
        },
    }
    blocks = [org]
    if svc is not None:
        service = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": svc["title"].replace("&amp;", "&"),
            "description": svc["intro"][:300],
            "provider": {"@type": "Organization", "name": NAP["name"]},
            "areaServed": "TR",
        }
        blocks.append(service)
    return "\n".join([
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in blocks
    ])


def page(title, current, body, extra_script="", lang="en", slug="index", svc=None, description=None):
    asset_prefix = "" if LANG_FOLDER[lang] == "" else "../"
    desc = description or META_DESC.get(lang, {}).get(slug, META_DESC["en"]["index"])
    dir_attr = "rtl" if lang == "ar" else "ltr"
    ar_font = '<link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">' if lang == "ar" else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Nora Paslanmaz ve Demir Celik</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} | Nora Paslanmaz ve Demir Celik">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{lang}">
{hreflang_tags(slug)}
<link rel="icon" type="image/png" href="{NORA_LOGO_PATH}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{ar_font}
<link rel="stylesheet" href="{asset_prefix}style.css">
{schema_org(lang, slug, svc=svc)}
</head>
<body>
{build_chrome(current, lang, slug)}
{body}
{footer_html(lang, slug)}
<script src="{asset_prefix}script.js"></script>
{f'<script>{extra_script}</script>' if extra_script else ''}
</body>
</html>
"""

# ---------------- HOME ----------------
home_body = f"""
<div class="hero-spacer" id="heroSpacer"></div>
<div class="hero-fixed" id="heroFixed">
  <div class="hero-viewport">
    <div class="hero-track" id="heroTrack"></div>
  </div>
  <div class="slide-label" id="slideLabel">
    <div class="slide-eyebrow" id="labelEyebrow">Service / 01</div>
    <h1 id="labelTitle">CNC Machining</h1>
    <div class="slide-rule"></div>
  </div>
  <div class="scroll-hint" id="scrollHint"><div class="line"></div>SCROLL</div>
</div>
<section class="home-highlights">
  <div class="wrap">
    <div class="hl-grid reveal">
      <div class="hl-intro">
        <span class="section-eyebrow">About Nora</span>
        <h2 class="section-title" style="margin-bottom:20px;">Manufacturing partner for stainless and steel.</h2>
        <p>With years of experience in the iron, steel, and stainless steel industry, Nora Paslanmaz ve Celik serves its customers through expertise, service quality, and competitively priced products, guided by a customer-first philosophy and a commitment to global quality standards.</p>
        <a class="more hl-download" href="../nora-company-profile.pdf" download="Nora-Company-Profile.pdf">Download Company Profile</a>
      </div>
      <div class="hl-certs">
        <span class="section-eyebrow">Certified</span>
        <div class="hl-cert-grid">
          <img src="{CERT_IMAGES['cert_iso9001']}" alt="ISO 9001:2015">
          <img src="{CERT_IMAGES['cert_iso14001']}" alt="ISO 14001:2015">
          <img src="{CERT_IMAGES['cert_iso45001']}" alt="ISO 45001:2018">
          <img src="{CERT_IMAGES['cert_iso10002']}" alt="ISO 10002:2018">
        </div>
        <a class="more" href="certificates.html">View All Certificates</a>
      </div>
    </div>
    <div class="hl-cta reveal">
      <h3>Ready to talk about your project?</h3>
      <a class="more" href="contact.html">Request a Quote</a>
    </div>
  </div>
</section>
"""
open(f"{EN_OUT_DIR}/index.html","w").write(page("Home","home",home_body,HERO_SCRIPT,slug="index"))

# ---------------- SERVICES ----------------
services_body = f"""
<section class="banner" style="background-image:url('{IMG_B64['plasma']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Services</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">Capabilities</span>
    <h2 class="section-title">Six processes, one facility, supply, cutting, bending, welding, and machining under one roof.</h2>
    <p style="font-family:'Poppins'; font-size:15px; color:var(--gray); max-width:640px; line-height:1.8; margin-top:18px; margin-bottom:56px;">Since our founding, Nora Paslanmaz ve Celik has stood out for its range of products, the durability and quality of what we make, and the level of service we offer, earning a leading position among firms in our sector. Backed by a large production capacity and an experienced, well-equipped team, we keep investing in our infrastructure to bring you supply, custom production, and processing under one roof.</p>
  </div>
  <div class="service-grid reveal-stagger">
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['bars']}')"></div>
      <div class="body">
        <span class="idx">01</span>
        <h3><a href="iron-steel-supply.html" style="color:inherit;">Iron &amp; Steel Supply</a></h3>
        <p>Sheet, profile, pipe, rolled stock, and steel mesh supplied directly, alongside related cutting and bending on request.</p>
        <a class="more" href="iron-steel-supply.html">Learn More</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['cutbend']}')"></div>
      <div class="body">
        <span class="idx">02</span>
        <h3><a href="cutting-bending.html" style="color:inherit;">Cutting and Bending</a></h3>
        <p>CNC press-brake bending across a range of thicknesses and tonnages, profiles, angles, and formed sheet.</p>
        <a class="more" href="cutting-bending.html">Learn More</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['cnc']}')"></div>
      <div class="body">
        <span class="idx">03</span>
        <h3><a href="cnc-machining.html" style="color:inherit;">CNC Machining</a></h3>
        <p>CNC turning, milling, drilling, and grinding to bring parts to exact dimension and surface finish.</p>
        <a class="more" href="cnc-machining.html">Learn More</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['welded_fab']}')"></div>
      <div class="body">
        <span class="idx">04</span>
        <h3><a href="welded-fabrication.html" style="color:inherit;">Welded Fabrication</a></h3>
        <p>Structural and custom welding across stainless, iron, aluminum, and steel, from single parts to full assemblies.</p>
        <a class="more" href="welded-fabrication.html">Learn More</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['plasma']}')"></div>
      <div class="body">
        <span class="idx">05</span>
        <h3><a href="plasma-cutting.html" style="color:inherit;">Plasma Cutting</a></h3>
        <p>High-speed ionized-gas cutting for steel and non-ferrous material up to 25mm, built for speed and low material waste.</p>
        <a class="more" href="plasma-cutting.html">Learn More</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['laser']}')"></div>
      <div class="body">
        <span class="idx">06</span>
        <h3><a href="laser-cutting.html" style="color:inherit;">Laser Cutting</a></h3>
        <p>Clean, high-precision laser cuts on stainless, iron, aluminum, and other sheet metals, complex shapes finished fast, with minimal production error.</p>
        <a class="more" href="laser-cutting.html">Learn More</a>
      </div>
    </div>
  </div>
</section>
"""
open(f"{EN_OUT_DIR}/services.html","w").write(page("Services","services",services_body,slug="services"))

# ---------------- PRODUCTS ----------------
demir_items = [
    ("kutu_profil", "Box Profile", "Kutu Profil Cesitleri"),
    ("metal_boru", "Metal Pipe", "Metal Boru Cesitleri"),
    ("kosebent", "Angle Steel", "Kosebent Cesitleri"),
    ("lama_demiri", "Flat Bar", "Lama Demiri"),
    ("silme_demiri", "Silme Bar", "Silme Demiri"),
    ("npu_demiri", "Structural Beams (NPU/NPI/IPE/HEA/HEB)", "NPU-NPI-IPE-HEA-HEB Demiri"),
    ("kare_demir", "Square Bar", "Kare Demir"),
    ("t_demir", "T-Bar", "T Demir"),
    ("transmisyon_mili", "Transmission Shaft", "Transmisyon Mili"),
    ("sac_cesitleri", "Sheet Metal", "Sac Cesitleri"),
    ("cati_panelleri", "Roof Panels", "Cati Panelleri"),
    ("cephe_panelleri", "Facade Panels", "Cephe Panelleri"),
    ("imalat_celigi", "Manufacturing Steel", "Imalat Celigi"),
    ("islah_celigi", "Heat-Treated Steel", "Islah Celigi"),
    ("otomat_celigi", "Free-Cutting Steel", "Otomat Celigi"),
    ("sementasyon_celigi", "Case-Hardening Steel", "Sementasyon Celigi"),
    ("shredder_knives", "Recycling Shredder Knives", "Geri Donusum Parcalayici Bicaklari"),
    ("constr_bucket_black", "Construction and Excavator Parts", "Insaat ve Ekskavator Parcalari"),
]

paslanmaz_items = [
    ("pas_sac_levha", "Stainless Sheet Plate", "Paslanmaz Sac Levha"),
    ("pas_profil", "Stainless Profile", "Paslanmaz Profil"),
    ("pas_lama", "Stainless Flat Bar", "Paslanmaz Lama"),
    ("pas_altikose", "Stainless Hexagon Bar", "Paslanmaz Altikose"),
    ("pas_dikisli_boru", "Stainless Welded Pipe", "Paslanmaz Dikisli Boru"),
    ("pas_dikissiz_boru", "Stainless Seamless Pipe", "Paslanmaz Dikissiz Boru"),
    ("pas_cubuk_mil", "Stainless Round Bar (Shaft)", "Paslanmaz Cubuk (Mil)"),
    ("pas_fittings", "Stainless Fittings", "Paslanmaz Fittings"),
]


# ================= INDIVIDUAL PRODUCT PAGES (24 products x 3 languages) =================
# Content is deliberately general/educational (what the material is, typical
# uses) rather than inventing specific dimensions, grades, or certifications
# we don't actually have data for. Exact specs are pointed to Contact.
PRODUCT_INFO = {
    "kutu_profil": {
        "en": {"what_is": "Box profile (also known as square or rectangular hollow section) is a steel section with a closed, hollow cross-section, formed by rolling and welding flat steel into a tube shape. Its closed profile gives it strong resistance to bending and torsion relative to its weight.",
               "applications": "Box profile is widely used in structural framing, fencing, gates, furniture frames, and general fabrication work where a strong, lightweight section is needed."},
        "tr": {"what_is": "Kutu profil, duz celigin haddelenip kaynaklanmasiyla olusturulan, kapali ve icicin bir kesite sahip celik bir urundur. Bu kapali kesit, agirligina oranla egilme ve burulmaya karsi guclu bir direnc saglar.",
               "applications": "Kutu profil; yapisal iskelet, cit, kapi, mobilya iskeleti ve genel imalat islerinde, guclu ve hafif bir profil gerektiginde yaygin olarak kullanilir."},
        "fr": {"what_is": "Le profilé carré (aussi appelé section creuse carrée ou rectangulaire) est une section en acier à section fermée et creuse, formée par laminage et soudure de tôle plate en forme de tube. Sa section fermée lui confère une bonne résistance à la flexion et à la torsion par rapport à son poids.",
               "applications": "Le profilé carré est largement utilisé pour l'ossature structurelle, les clôtures, les portails, les cadres de mobilier et les travaux de fabrication générale nécessitant une section solide et légère."},
        "ar": {"what_is": "القوطي (المعروف أيضًا بالقطاع المجوف المربع أو المستطيل) هو قطاع فولاذي ذو مقطع مغلق ومجوف، يُشكّل بلف ولحام الصلب المسطح على شكل أنبوب. يمنحه مقطعه المغلق مقاومة قوية للانحناء والالتواء بالنسبة إلى وزنه.",
               "applications": "يُستخدم القوطي على نطاق واسع في الهياكل الإنشائية والأسوار والبوابات وهياكل الأثاث وأعمال التصنيع العامة حيث تكون هناك حاجة إلى قطاع قوي وخفيف الوزن."},
    },
    "metal_boru": {
        "en": {"what_is": "Metal pipe is a hollow cylindrical section used to carry fluids or gases, or as a structural element in its own right. It can be produced as welded pipe, formed from rolled steel with a seam, or seamless pipe, extruded without a joint.",
               "applications": "Metal pipe is used across plumbing, structural framing, scaffolding, handrails, and industrial piping systems."},
        "tr": {"what_is": "Metal boru, sivi veya gaz tasimak ya da baslli basina yapisal bir eleman olarak kullanilan icicin, silindirik bir kesittir. Kaynakli boru (haddelenmis celikten dikisli) veya dikissiz boru (eksiz ekstrude) olarak uretilebilir.",
               "applications": "Metal boru; tesisat, yapisal iskelet, iskele, korkuluk ve endustriyel boru hatti sistemlerinde kullanilir."},
        "fr": {"what_is": "Le tube métallique est une section cylindrique creuse utilisée pour transporter des fluides ou des gaz, ou comme élément structurel à part entière. Il peut être produit sous forme de tube soudé, formé à partir d'acier laminé avec une soudure, ou de tube sans soudure, extrudé sans jointure.",
               "applications": "Le tube métallique est utilisé en plomberie, ossature structurelle, échafaudage, mains courantes et réseaux de tuyauterie industrielle."},
        "ar": {"what_is": "الأنبوب المعدني هو مقطع أسطواني مجوف يُستخدم لنقل السوائل أو الغازات، أو كعنصر إنشائي بحد ذاته. يمكن إنتاجه كأنبوب ملحوم، مُشكّل من صلب مدرفل بخط لحام، أو أنبوب سلس مُبثوق دون وصلة.",
               "applications": "يُستخدم الأنبوب المعدني في السباكة والهياكل الإنشائية والسقالات والدرابزين وأنظمة الأنابيب الصناعية."},
    },
    "kosebent": {
        "en": {"what_is": "Angle steel is an L-shaped structural section, formed from two flat legs joined at a right angle. It's one of the most common structural shapes because of how efficiently it resists bending along two axes at once.",
               "applications": "Angle steel is used in structural framing, brackets, shelving, towers, and as a reinforcing or connecting element in fabrication work."},
        "tr": {"what_is": "Kosebent, birbirine dik acida birlesen iki duz kenardan olusan L seklinde yapisal bir profildir. Aynı anda iki eksende egilmeye karsi verimli direnci sayesinde en yaygin kullanilan yapisal sekillerden biridir.",
               "applications": "Kosebent; yapisal iskelet, braket, raf, kule ve imalat islerinde takviye veya baglanti elemani olarak kullanilir."},
        "fr": {"what_is": "La cornière est une section structurelle en forme de L, formée de deux ailes plates jointes à angle droit. C'est l'une des formes structurelles les plus courantes en raison de sa résistance efficace à la flexion selon deux axes à la fois.",
               "applications": "La cornière est utilisée pour l'ossature structurelle, les supports, les étagères, les tours, et comme élément de renfort ou de liaison dans les travaux de fabrication."},
        "ar": {"what_is": "زاوية الحديد هي قطاع إنشائي على شكل حرف L، يتكون من ضلعين مسطحين متصلين بزاوية قائمة. وهي من أكثر الأشكال الإنشائية شيوعًا لكفاءتها في مقاومة الانحناء على محورين في آن واحد.",
               "applications": "تُستخدم زاوية الحديد في الهياكل الإنشائية والكتائف والأرفف والأبراج، وكعنصر تقوية أو ربط في أعمال التصنيع."},
    },
    "lama_demiri": {
        "en": {"what_is": "Flat bar is a rectangular steel section, flat and rolled to a consistent thickness and width. It's one of the most versatile raw steel forms, used as a starting material for further cutting, welding, or machining.",
               "applications": "Flat bar is used for framing, brackets, gates, railings, and as stock material for further fabrication."},
        "tr": {"what_is": "Lama demiri, sabit kalinlik ve genislikte haddelenmis, dikdortgen kesitli duz bir celik urundur. Kesim, kaynak veya islemenin baslangic malzemesi olarak kullanilan en cok yonlu ham celik formlarindan biridir.",
               "applications": "Lama demiri; iskelet, braket, kapi, korkuluk ve ileri imalat icin ham malzeme olarak kullanilir."},
        "fr": {"what_is": "Le fer plat est une section en acier rectangulaire, plate et laminée à une épaisseur et une largeur constantes. C'est l'une des formes d'acier brut les plus polyvalentes, utilisée comme matière première pour la découpe, la soudure ou l'usinage.",
               "applications": "Le fer plat est utilisé pour l'ossature, les supports, les portails, les garde-corps, et comme matière première pour la fabrication."},
        "ar": {"what_is": "حديد اللامة هو قطاع فولاذي مستطيل، مسطح ومدرفل بسماكة وعرض ثابتين. وهو من أكثر أشكال الصلب الخام تعدد استخدامًا، يُستخدم كمادة أولية للقص أو اللحام أو التشغيل الإضافي.",
               "applications": "يُستخدم حديد اللامة في الهياكل والكتائف والبوابات والدرابزين، وكمادة خام لمزيد من التصنيع."},
    },
    "silme_demiri": {
        "en": {"what_is": "Silme bar is a narrow flat steel strip, thinner than standard flat bar, typically used for trim, edging, and light structural work.",
               "applications": "Silme bar is commonly used for edging, trim work, light bracketry, and decorative metalwork."},
        "tr": {"what_is": "Silme demiri, standart lama demirinden daha ince, dar ve duz bir celik seritdir, genellikle kenar bitirme ve hafif yapisal islerde kullanilir.",
               "applications": "Silme demiri; kenar bitirme, dekoratif metal isleri ve hafif braket uygulamalarinda yaygin olarak kullanilir."},
        "fr": {"what_is": "Le fer silme est une bande d'acier plate et étroite, plus fine que le fer plat standard, généralement utilisée pour les finitions, les bordures et les travaux structurels légers.",
               "applications": "Le fer silme est couramment utilisé pour les bordures, les finitions, les petits supports et la ferronnerie décorative."},
        "ar": {"what_is": "حديد السلمة هو شريط فولاذي مسطح وضيق، أرفع من حديد اللامة القياسي، يُستخدم عادةً للتشطيب والحواف والأعمال الإنشائية الخفيفة.",
               "applications": "يُستخدم حديد السلمة بشكل شائع في تشطيب الحواف والأعمال الديكورية المعدنية والكتائف الخفيفة."},
    },
    "npu_demiri": {
        "en": {"what_is": "Structural beams such as NPU, NPI, IPE, HEA, and HEB sections are hot-rolled steel profiles with a distinct cross-sectional shape (U-channel or I/H-beam), engineered to carry heavy structural loads efficiently.",
               "applications": "These beams form the structural skeleton of buildings, bridges, and heavy industrial structures, wherever load-bearing strength is the primary requirement."},
        "tr": {"what_is": "NPU, NPI, IPE, HEA ve HEB gibi yapisal kirisler, agir yapisal yukleri verimli sekilde tasimak uzere tasarlanmis, belirgin bir kesit sekline (U profili veya I/H kiris) sahip sicak haddelenmis celik profillerdir.",
               "applications": "Bu kirisler; bina, kopru ve agir endustriyel yapilarin tasiyici iskeletini olusturur, tasima gucunun oncelik oldugu her yerde kullanilir."},
        "fr": {"what_is": "Les poutrelles structurelles telles que les profilés NPU, NPI, IPE, HEA et HEB sont des profilés en acier laminé à chaud, à section distincte (en U ou en I/H), conçues pour supporter efficacement de lourdes charges structurelles.",
               "applications": "Ces poutrelles forment l'ossature structurelle des bâtiments, des ponts et des structures industrielles lourdes, partout où la résistance porteuse est l'exigence principale."},
        "ar": {"what_is": "الكمرات الإنشائية مثل NPU وNPI وIPE وHEA وHEB هي قطاعات فولاذية مدرفلة على الساخن ذات مقطع مميز (قناة على شكل U أو كمرة I/H)، مصممة لتحمل الأحمال الإنشائية الثقيلة بكفاءة.",
               "applications": "تُشكّل هذه الكمرات الهيكل العظمي الإنشائي للمباني والجسور والمنشآت الصناعية الثقيلة، حيثما كانت قوة التحمل هي المتطلب الأساسي."},
    },
    "kare_demir": {
        "en": {"what_is": "Square bar is solid steel stock with a square cross-section, rolled to a consistent size along its length.",
               "applications": "Square bar is used in fabrication, railings, gates, machine parts, and as raw stock for further machining."},
        "tr": {"what_is": "Kare demir, boyu boyunca sabit olcude haddelenmis, kare kesitli dolu bir celik urunudur.",
               "applications": "Kare demir; imalat, korkuluk, kapi, makine parcalari ve ileri isleme icin ham stok olarak kullanilir."},
        "fr": {"what_is": "Le fer carré est une barre d'acier pleine à section carrée, laminée à une dimension constante sur toute sa longueur.",
               "applications": "Le fer carré est utilisé en fabrication, garde-corps, portails, pièces de machines, et comme matière première pour l'usinage."},
        "ar": {"what_is": "الحديد المربع هو قضيب فولاذي صلب ذو مقطع مربع، مدرفل بمقاس ثابت على طول امتداده.",
               "applications": "يُستخدم الحديد المربع في التصنيع والدرابزين والبوابات وأجزاء الآلات، وكمادة خام لمزيد من التشغيل."},
    },
    "t_demir": {
        "en": {"what_is": "T-bar is a structural steel section shaped like the letter T, combining a flat top flange with a vertical web.",
               "applications": "T-bar is used in framing, support structures, and applications needing a stiffening edge, such as shelving and trim work."},
        "tr": {"what_is": "T demir, duz bir ust baski ile dikey bir govdeyi birlestiren, T harfi seklinde yapisal bir celik profildir.",
               "applications": "T demir; iskelet, destek yapilari ve raf ile bitirme isleri gibi sertlestirici kenar gerektiren uygulamalarda kullanilir."},
        "fr": {"what_is": "Le fer en T est une section en acier structurel en forme de T, combinant une aile plate supérieure et une âme verticale.",
               "applications": "Le fer en T est utilisé pour l'ossature, les structures de support, et les applications nécessitant un bord rigidifiant, comme les étagères et les finitions."},
        "ar": {"what_is": "حديد T هو قطاع فولاذي إنشائي على شكل الحرف T، يجمع بين جناح علوي مسطح وجذع عمودي.",
               "applications": "يُستخدم حديد T في الهياكل وبنى الدعم والتطبيقات التي تحتاج إلى حافة تصلّب، مثل الأرفف وأعمال التشطيب."},
    },
    "transmisyon_mili": {
        "en": {"what_is": "Transmission shaft is solid round steel bar, precision-rolled or turned, designed to transmit rotational force in mechanical systems.",
               "applications": "Transmission shaft is used in machinery, drivetrains, and mechanical assemblies requiring a precise, load-bearing rotating shaft."},
        "tr": {"what_is": "Transmisyon mili, mekanik sistemlerde donme kuvvetini iletmek uzere tasarlanmis, hassas haddelenmis veya islenmis dolu yuvarlak bir celik cubuktur.",
               "applications": "Transmisyon mili; hassas, yuk tasiyan donen bir mil gerektiren makine, aktarma organlari ve mekanik montajlarda kullanilir."},
        "fr": {"what_is": "L'arbre de transmission est une barre d'acier ronde pleine, laminée ou tournée avec précision, conçue pour transmettre une force de rotation dans les systèmes mécaniques.",
               "applications": "L'arbre de transmission est utilisé dans les machines, les transmissions et les ensembles mécaniques nécessitant un arbre rotatif précis et porteur."},
        "ar": {"what_is": "عمود نقل الحركة هو قضيب فولاذي مستدير صلب، مدرفل أو مخروط بدقة، مصمم لنقل قوة الدوران في الأنظمة الميكانيكية.",
               "applications": "يُستخدم عمود نقل الحركة في الآلات وأنظمة نقل الحركة والتجميعات الميكانيكية التي تتطلب عمودًا دوارًا دقيقًا وقادرًا على تحمل الأحمال."},
    },
    "sac_cesitleri": {
        "en": {"what_is": "Sheet metal is flat-rolled steel supplied in large sheets or coils, available in a range of thicknesses and finishes.",
               "applications": "Sheet metal is a base material for laser cutting, plasma cutting, and bending work across construction, automotive, and general fabrication."},
        "tr": {"what_is": "Sac, buyuk levhalar veya ruloler halinde tedarik edilen, cesitli kalinlik ve yuzey seceneklerine sahip duz haddelenmis celiktir.",
               "applications": "Sac; insaat, otomotiv ve genel imalatta lazer kesim, plazma kesim ve bukum islerinin temel malzemesidir."},
        "fr": {"what_is": "La tôle est de l'acier laminé plat fourni en grandes feuilles ou en bobines, disponible dans une gamme d'épaisseurs et de finitions.",
               "applications": "La tôle est une matière de base pour la découpe laser, la découpe plasma et le pliage dans le bâtiment, l'automobile et la fabrication générale."},
        "ar": {"what_is": "الصاج هو صلب مدرفل مسطح يُورّد على شكل ألواح كبيرة أو لفائف، متوفر بمجموعة من السماكات والتشطيبات.",
               "applications": "الصاج هو المادة الأساسية لأعمال القص بالليزر والبلازما والثني في قطاعات البناء والسيارات والتصنيع العام."},
    },
    "cati_panelleri": {
        "en": {"what_is": "Roof panels are pre-formed steel sheets, typically profiled with ribs or corrugations, engineered for weather-resistant roof cladding.",
               "applications": "Roof panels are used for industrial, commercial, and agricultural building roofs where durability and weather resistance matter."},
        "tr": {"what_is": "Cati panelleri, genellikle oluklu veya dalgali profile sahip, hava kosullarina dayanikli cati kaplamasi icin tasarlanmis on formlu celik levhalardir.",
               "applications": "Cati panelleri; dayaniklilik ve hava kosullarina direncin onemli oldugu endustriyel, ticari ve tarimsal bina catilarinda kullanilir."},
        "fr": {"what_is": "Les panneaux de toiture sont des tôles d'acier préformées, généralement profilées avec des nervures ou des ondulations, conçues pour un bardage de toit résistant aux intempéries.",
               "applications": "Les panneaux de toiture sont utilisés pour les toits de bâtiments industriels, commerciaux et agricoles où la durabilité et la résistance aux intempéries comptent."},
        "ar": {"what_is": "ألواح الأسقف هي صفائح فولاذية مُشكّلة مسبقًا، عادةً ما تكون مضلعة أو مموجة، مصممة لتغطية أسقف مقاومة للعوامل الجوية.",
               "applications": "تُستخدم ألواح الأسقف لأسقف المباني الصناعية والتجارية والزراعية حيث تهم المتانة ومقاومة العوامل الجوية."},
    },
    "cephe_panelleri": {
        "en": {"what_is": "Facade panels are formed steel sheets used to clad the exterior walls of a building, combining structural cladding with an architectural finish.",
               "applications": "Facade panels are used for the exterior walls of industrial and commercial buildings, providing weather protection and a finished appearance."},
        "tr": {"what_is": "Cephe panelleri, bir binanin dis duvarlarini kaplamak icin kullanilan, yapisal kaplamayi mimari bir gorunumle birlestiren sekillendirilmis celik levhalardir.",
               "applications": "Cephe panelleri; endustriyel ve ticari binalarin dis duvarlarinda, hava korumasi ve dus bir gorunum saglamak icin kullanilir."},
        "fr": {"what_is": "Les panneaux de façade sont des tôles d'acier formées utilisées pour habiller les murs extérieurs d'un bâtiment, associant un bardage structurel à une finition architecturale.",
               "applications": "Les panneaux de façade sont utilisés pour les murs extérieurs de bâtiments industriels et commerciaux, offrant une protection contre les intempéries et une finition soignée."},
        "ar": {"what_is": "ألواح الواجهات هي صفائح فولاذية مُشكّلة تُستخدم لكسوة الجدران الخارجية للمبنى، تجمع بين الكسوة الإنشائية واللمسة المعمارية.",
               "applications": "تُستخدم ألواح الواجهات للجدران الخارجية للمباني الصناعية والتجارية، توفر حماية من العوامل الجوية ومظهرًا نهائيًا متكاملًا."},
    },
    "imalat_celigi": {
        "en": {"what_is": "Manufacturing steel refers to general-purpose carbon steel supplied as raw stock for machining and fabrication, chosen for its consistent, workable properties.",
               "applications": "Manufacturing steel is used as base stock across general machining, fabrication, and parts production."},
        "tr": {"what_is": "Imalat celigi, tutarli ve islenebilir ozellikleri nedeniyle secilen, isleme ve imalat icin ham stok olarak tedarik edilen genel amacli karbon celigidir.",
               "applications": "Imalat celigi; genel isleme, imalat ve parca uretiminde temel stok malzeme olarak kullanilir."},
        "fr": {"what_is": "L'acier de construction désigne un acier au carbone à usage général, fourni comme matière première pour l'usinage et la fabrication, apprécié pour ses propriétés constantes et faciles à travailler.",
               "applications": "L'acier de construction est utilisé comme matière première dans l'usinage général, la fabrication et la production de pièces."},
        "ar": {"what_is": "صلب التصنيع يشير إلى صلب كربوني عام الغرض يُورّد كمادة خام للتشغيل والتصنيع، يُختار لخصائصه الثابتة القابلة للتشغيل.",
               "applications": "يُستخدم صلب التصنيع كمادة خام أساسية في التشغيل العام والتصنيع وإنتاج القطع."},
    },
    "islah_celigi": {
        "en": {"what_is": "Heat-treated steel (also called quenched and tempered steel) has undergone a controlled heating and cooling process to increase its strength and hardness beyond that of standard carbon steel.",
               "applications": "Heat-treated steel is used for machine parts, tooling, and components requiring higher strength and wear resistance than standard steel."},
        "tr": {"what_is": "Islah celigi, standart karbon celiginin otesinde mukavemet ve sertlik kazandirmak icin kontrollu bir isitma ve sogutma islemine tabi tutulmus celiktir.",
               "applications": "Islah celigi; standart celikten daha yuksek mukavemet ve asinma direnci gerektiren makine parcalari, takim ve bilesenlerde kullanilir."},
        "fr": {"what_is": "L'acier trempé (également appelé acier trempé et revenu) a subi un processus contrôlé de chauffage et de refroidissement pour augmenter sa résistance et sa dureté au-delà de celles de l'acier au carbone standard.",
               "applications": "L'acier trempé est utilisé pour les pièces de machines, l'outillage et les composants nécessitant une résistance et une résistance à l'usure supérieures à l'acier standard."},
        "ar": {"what_is": "الصلب المعالج حراريًا (يُعرف أيضًا بالصلب المقسّى والمُلطّف) خضع لعملية تسخين وتبريد مضبوطة لزيادة قوته وصلابته بما يتجاوز الصلب الكربوني القياسي.",
               "applications": "يُستخدم الصلب المعالج حراريًا في أجزاء الآلات والعدد والمكونات التي تتطلب قوة ومقاومة تآكل أعلى من الصلب القياسي."},
    },
    "otomat_celigi": {
        "en": {"what_is": "Free-cutting steel (also known as free-machining steel) is a steel alloy formulated with additives such as sulfur to improve machinability, producing cleaner cuts and longer tool life.",
               "applications": "Free-cutting steel is used for high-volume, precision-machined parts where fast, clean machining matters."},
        "tr": {"what_is": "Otomat celigi (serbest islenebilir celik), islenebilirligi artirmak icin kukurt gibi katkilarla formule edilmis, daha temiz kesim ve daha uzun takim omru saglayan bir celik alasimidir.",
               "applications": "Otomat celigi; hizli ve temiz islemenin onemli oldugu, yuksek hacimli ve hassas islenmis parcalarda kullanilir."},
        "fr": {"what_is": "L'acier de décolletage (aussi appelé acier de coupe facile) est un alliage d'acier formulé avec des additifs tels que le soufre pour améliorer l'usinabilité, produisant des coupes plus nettes et une durée de vie d'outil plus longue.",
               "applications": "L'acier de décolletage est utilisé pour les pièces usinées de précision à grand volume, où un usinage rapide et propre est essentiel."},
        "ar": {"what_is": "صلب التشغيل الحر (يُعرف أيضًا بصلب التشغيل السريع) هو سبيكة صلب مُركّبة بإضافات مثل الكبريت لتحسين قابلية التشغيل، مما ينتج قطعًا أنظف وعمرًا أطول للأدوات.",
               "applications": "يُستخدم صلب التشغيل الحر للقطع المُشغّلة بدقة وبكميات كبيرة حيث يهم التشغيل السريع والنظيف."},
    },
    "sementasyon_celigi": {
        "en": {"what_is": "Case-hardening steel is a low-carbon steel designed to be surface-hardened through a carburizing heat treatment, giving it a hard outer surface while retaining a tougher, more ductile core.",
               "applications": "Case-hardening steel is used for gears, pins, and mechanical parts that need a wear-resistant surface combined with impact toughness."},
        "tr": {"what_is": "Sementasyon celigi, sement (karbonlama) isil islemi ile yuzeyi sertlestirilmek uzere tasarlanmis, sert bir dis yuzeye sahipken daha tokluk ve suneklik saglayan bir cekirdek koruyan dusuk karbonlu celiktir.",
               "applications": "Sementasyon celigi; asinmaya dayanikli bir yuzey ile darbe tokluguna ihtiyac duyan disli, pim ve mekanik parcalarda kullanilir."},
        "fr": {"what_is": "L'acier de cémentation est un acier à faible teneur en carbone conçu pour être durci en surface par un traitement thermique de cémentation, lui donnant une surface externe dure tout en conservant un cœur plus résistant et ductile.",
               "applications": "L'acier de cémentation est utilisé pour les engrenages, les axes et les pièces mécaniques nécessitant une surface résistante à l'usure combinée à une bonne résilience aux chocs."},
        "ar": {"what_is": "صلب التصليد السطحي هو صلب منخفض الكربون مصمم ليُصلّد سطحيًا من خلال معالجة حرارية بالكربنة، مما يمنحه سطحًا خارجيًا صلبًا مع الحفاظ على لُب أكثر متانة ومرونة.",
               "applications": "يُستخدم صلب التصليد السطحي في التروس والمحاور والأجزاء الميكانيكية التي تحتاج إلى سطح مقاوم للتآكل مع متانة ضد الصدمات."},
    },
    "pas_sac_levha": {
        "en": {"what_is": "Stainless sheet plate is flat-rolled stainless steel, combining the corrosion resistance of stainless with the flat, workable form of sheet metal.",
               "applications": "Stainless sheet plate is used across food processing, kitchen equipment, architecture, and any application needing a hygienic, corrosion-resistant surface."},
        "tr": {"what_is": "Paslanmaz sac levha, paslanmaz celigin korozyon direncini sacin duz ve islenebilir formuyla birlestiren duz haddelenmis paslanmaz celiktir.",
               "applications": "Paslanmaz sac levha; gida isleme, mutfak ekipmanlari, mimari ve hijyenik, korozyona dayanikli yuzey gerektiren her uygulamada kullanilir."},
        "fr": {"what_is": "La tôle inox est de l'acier inoxydable laminé plat, combinant la résistance à la corrosion de l'inox avec la forme plate et facile à travailler de la tôle.",
               "applications": "La tôle inox est utilisée dans l'agroalimentaire, les équipements de cuisine, l'architecture, et toute application nécessitant une surface hygiénique et résistante à la corrosion."},
        "ar": {"what_is": "صاج الستانلس ستيل هو صلب مقاوم للصدأ مدرفل مسطح، يجمع بين مقاومة التآكل الخاصة بالستانلس ستيل والشكل المسطح القابل للتشغيل الخاص بالصاج.",
               "applications": "يُستخدم صاج الستانلس ستيل في تصنيع الأغذية ومعدات المطابخ والعمارة وأي تطبيق يحتاج إلى سطح صحي مقاوم للتآكل."},
    },
    "pas_profil": {
        "en": {"what_is": "Stainless profile covers stainless steel structural sections, formed to standard profile shapes while retaining stainless steel's corrosion resistance.",
               "applications": "Stainless profile is used in architecture, food processing equipment, and structural applications exposed to moisture or corrosive environments."},
        "tr": {"what_is": "Paslanmaz profil, paslanmaz celigin korozyon direncini korurken standart profil sekillerine getirilmis paslanmaz celik yapisal kesitleri kapsar.",
               "applications": "Paslanmaz profil; mimari, gida isleme ekipmanlari ve neme veya korozif ortamlara maruz kalan yapisal uygulamalarda kullanilir."},
        "fr": {"what_is": "Le profilé inox regroupe les sections structurelles en acier inoxydable, formées selon des profils standards tout en conservant la résistance à la corrosion de l'inox.",
               "applications": "Le profilé inox est utilisé en architecture, dans les équipements agroalimentaires et les applications structurelles exposées à l'humidité ou aux environnements corrosifs."},
        "ar": {"what_is": "بروفايل الستانلس ستيل يشمل القطاعات الإنشائية من الستانلس ستيل، مُشكّلة بأشكال بروفايل قياسية مع الحفاظ على مقاومة التآكل الخاصة بالستانلس ستيل.",
               "applications": "يُستخدم بروفايل الستانلس ستيل في العمارة ومعدات تصنيع الأغذية والتطبيقات الإنشائية المعرضة للرطوبة أو البيئات المسببة للتآكل."},
    },
    "pas_lama": {
        "en": {"what_is": "Stainless flat bar is rectangular stainless steel stock, flat and rolled to consistent dimensions.",
               "applications": "Stainless flat bar is used for brackets, trim, and fabrication work needing corrosion resistance."},
        "tr": {"what_is": "Paslanmaz lama, sabit olculerde haddelenmis, duz dikdortgen kesitli paslanmaz celik stokdur.",
               "applications": "Paslanmaz lama; korozyon direnci gerektiren braket, kenar bitirme ve imalat islerinde kullanilir."},
        "fr": {"what_is": "Le fer plat inox est une barre d'acier inoxydable rectangulaire, plate et laminée à des dimensions constantes.",
               "applications": "Le fer plat inox est utilisé pour les supports, les finitions et les travaux de fabrication nécessitant une résistance à la corrosion."},
        "ar": {"what_is": "لامة الستانلس ستيل هي مادة خام مستطيلة من الستانلس ستيل، مسطحة ومدرفلة بأبعاد ثابتة.",
               "applications": "تُستخدم لامة الستانلس ستيل للكتائف والتشطيبات وأعمال التصنيع التي تحتاج إلى مقاومة التآكل."},
    },
    "pas_altikose": {
        "en": {"what_is": "Stainless hexagon bar is solid stainless steel stock with a hexagonal cross-section, commonly used where a flat-sided bar is needed for grip or fastening.",
               "applications": "Stainless hexagon bar is used for fasteners, fittings, and machined parts requiring corrosion resistance."},
        "tr": {"what_is": "Paslanmaz altikose, kavrama veya sikma icin duz yuzeyli bir cubuk gerektiginde kullanilan, altigen kesitli dolu paslanmaz celik stoktur.",
               "applications": "Paslanmaz altikose; korozyon direnci gerektiren baglanti elemanlari, fittings ve islenmis parcalarda kullanilir."},
        "fr": {"what_is": "La barre hexagonale inox est une barre pleine en acier inoxydable à section hexagonale, couramment utilisée lorsqu'une barre à faces plates est nécessaire pour la prise ou le serrage.",
               "applications": "La barre hexagonale inox est utilisée pour les fixations, les raccords et les pièces usinées nécessitant une résistance à la corrosion."},
        "ar": {"what_is": "السداسي من الستانلس ستيل هو مادة خام صلبة ذات مقطع سداسي، تُستخدم عادةً حيث تكون هناك حاجة إلى قضيب ذي أوجه مسطحة للإمساك أو الربط.",
               "applications": "يُستخدم السداسي من الستانلس ستيل في مواسير الربط والتجهيزات والقطع المُشغّلة التي تتطلب مقاومة التآكل."},
    },
    "pas_dikisli_boru": {
        "en": {"what_is": "Stainless welded pipe is stainless steel pipe formed by rolling and welding a seam along its length.",
               "applications": "Stainless welded pipe is used in piping systems, railings, and structural work requiring corrosion resistance at a lower cost than seamless pipe."},
        "tr": {"what_is": "Paslanmaz dikisli boru, boyu boyunca haddelenip kaynaklanarak olusturulan paslanmaz celik borudur.",
               "applications": "Paslanmaz dikisli boru; dikissiz boruya gore daha dusuk maliyetle korozyon direnci gerektiren boru hatti, korkuluk ve yapisal islerde kullanilir."},
        "fr": {"what_is": "Le tube inox soudé est un tube en acier inoxydable formé par laminage et soudure d'une jointure sur toute sa longueur.",
               "applications": "Le tube inox soudé est utilisé dans les réseaux de tuyauterie, les garde-corps et les travaux structurels nécessitant une résistance à la corrosion à moindre coût que le tube sans soudure."},
        "ar": {"what_is": "أنبوب الستانلس ستيل الملحوم هو أنبوب من الستانلس ستيل يُشكّل بلف ولحام خط على طول امتداده.",
               "applications": "يُستخدم أنبوب الستانلس الملحوم في أنظمة الأنابيب والدرابزين والأعمال الإنشائية التي تتطلب مقاومة التآكل بتكلفة أقل من الأنبوب السلس."},
    },
    "pas_dikissiz_boru": {
        "en": {"what_is": "Stainless seamless pipe is stainless steel pipe extruded without a weld seam, giving it consistent strength along its entire length.",
               "applications": "Stainless seamless pipe is used in higher-pressure or higher-purity applications such as food, chemical, and pharmaceutical processing."},
        "tr": {"what_is": "Paslanmaz dikissiz boru, kaynak dikisi olmadan ekstrude edilen, boyu boyunca tutarli mukavemet saglayan paslanmaz celik borudur.",
               "applications": "Paslanmaz dikissiz boru; gida, kimya ve ilac isleme gibi daha yuksek basinc veya saflik gerektiren uygulamalarda kullanilir."},
        "fr": {"what_is": "Le tube inox sans soudure est un tube en acier inoxydable extrudé sans jointure soudée, lui conférant une résistance constante sur toute sa longueur.",
               "applications": "Le tube inox sans soudure est utilisé dans les applications à haute pression ou haute pureté telles que l'agroalimentaire, la chimie et le pharmaceutique."},
        "ar": {"what_is": "أنبوب الستانلس ستيل السلس هو أنبوب من الستانلس ستيل مُبثوق دون خط لحام، مما يمنحه قوة ثابتة على طول امتداده بالكامل.",
               "applications": "يُستخدم أنبوب الستانلس السلس في التطبيقات ذات الضغط العالي أو النقاء العالي مثل تصنيع الأغذية والكيماويات والأدوية."},
    },
    "pas_cubuk_mil": {
        "en": {"what_is": "Stainless round bar (shaft) is solid, cylindrical stainless steel stock, precision-rolled or turned for use as a shaft or machined component.",
               "applications": "Stainless round bar is used for shafts, fasteners, and machined parts requiring corrosion resistance and dimensional precision."},
        "tr": {"what_is": "Paslanmaz cubuk (mil), mil veya islenmis bilesen olarak kullanilmak uzere hassas haddelenmis veya islenmis, dolu silindirik paslanmaz celik stoktur.",
               "applications": "Paslanmaz cubuk (mil); korozyon direnci ve boyutsal hassasiyet gerektiren mil, baglanti elemani ve islenmis parcalarda kullanilir."},
        "fr": {"what_is": "La barre ronde inox (arbre) est une matière première cylindrique pleine en acier inoxydable, laminée ou tournée avec précision pour servir d'arbre ou de composant usiné.",
               "applications": "La barre ronde inox est utilisée pour les arbres, les fixations et les pièces usinées nécessitant une résistance à la corrosion et une précision dimensionnelle."},
        "ar": {"what_is": "قضيب/عمود الستانلس المستدير هو مادة خام أسطوانية صلبة من الستانلس ستيل، مدرفلة أو مخروطة بدقة للاستخدام كعمود أو مكوّن مُشغّل.",
               "applications": "يُستخدم قضيب الستانلس المستدير للأعمدة ومواسير الربط والقطع المُشغّلة التي تتطلب مقاومة التآكل والدقة البُعدية."},
    },
    "pas_fittings": {
        "en": {"what_is": "Stainless fittings are pre-formed stainless steel components, such as elbows, tees, and couplings, used to join and route piping systems.",
               "applications": "Stainless fittings are used wherever stainless pipe needs to be joined, branched, or redirected, particularly in food, chemical, and plumbing systems."},
        "tr": {"what_is": "Paslanmaz fittings; boru hatlarini birlestirmek ve yonlendirmek icin kullanilan dirsek, te ve kuplaj gibi on formlu paslanmaz celik bilesenlerdir.",
               "applications": "Paslanmaz fittings; ozellikle gida, kimya ve tesisat sistemlerinde paslanmaz borunun birlestirilmesi, dallandirilmasi veya yonlendirilmesi gereken her yerde kullanilir."},
        "fr": {"what_is": "Les raccords inox sont des composants préformés en acier inoxydable, tels que coudes, tés et manchons, utilisés pour joindre et orienter les réseaux de tuyauterie.",
               "applications": "Les raccords inox sont utilisés partout où un tube inox doit être joint, dérivé ou réorienté, notamment dans l'agroalimentaire, la chimie et la plomberie."},
        "ar": {"what_is": "وصلات الستانلس ستيل هي مكونات مُشكّلة مسبقًا من الستانلس ستيل، مثل الأكواع والتيهات والوصلات، تُستخدم لربط وتوجيه أنظمة الأنابيب.",
               "applications": "تُستخدم وصلات الستانلس ستيل أينما احتاج أنبوب الستانلس إلى الربط أو التفرع أو إعادة التوجيه، خاصة في أنظمة الأغذية والكيماويات والسباكة."},
    },
    "shredder_knives": {
        "en": {"what_is": "Recycling shredder knives are heavy-duty cutting blades and wear parts engineered for industrial shredding and recycling machinery, built to withstand continuous high-impact cutting cycles.",
               "applications": "Recycling shredder knives are used in scrap processing, waste recycling, and material shredding lines where durable, replaceable cutting edges are essential to keep equipment running."},
        "tr": {"what_is": "Geri donusum parcalayici bicaklari, endustriyel parcalama ve geri donusum makineleri icin tasarlanmis, surekli yuksek darbeli kesim dongulerine dayanacak agir hizmet tipi kesici bicaklar ve asinma parcalaridir.",
               "applications": "Geri donusum parcalayici bicaklari; hurda isleme, atik geri donusumu ve malzeme parcalama hatlarinda, ekipmanin calismaya devam etmesi icin dayanikli ve degistirilebilir kesici kenarlarin gerekli oldugu yerlerde kullanilir."},
        "fr": {"what_is": "Les lames de broyeur de recyclage sont des lames de coupe et des pièces d'usure robustes conçues pour les machines industrielles de broyage et de recyclage, capables de résister à des cycles de coupe continus à fort impact.",
               "applications": "Les lames de broyeur de recyclage sont utilisées dans le traitement de la ferraille, le recyclage des déchets et les lignes de broyage de matériaux, là où des arêtes de coupe durables et remplaçables sont essentielles."},
        "ar": {"what_is": "شفرات آلة تقطيع إعادة التدوير هي شفرات قطع وقطع مقاومة للتآكل مصممة للآلات الصناعية للتقطيع وإعادة التدوير، قادرة على تحمل دورات قطع مستمرة عالية التأثير.",
               "applications": "تُستخدم شفرات آلة التقطيع في معالجة الخردة وإعادة تدوير النفايات وخطوط تقطيع المواد، حيث تكون حواف القطع المتينة والقابلة للاستبدال ضرورية."},
    },
    "constr_bucket_black": {
        "en": {"what_is": "Construction and excavator parts cover heavy steel attachments and structural components for construction machinery, including buckets, forks, and boom components, fabricated to handle demanding site conditions.",
               "applications": "These parts are used on excavators, skid steers, and loaders across construction, demolition, and earthmoving work."},
        "tr": {"what_is": "Insaat ve ekskavator parcalari, kova, catal ve bum bilesenleri dahil olmak uzere insaat makineleri icin agir celik ekleri ve yapisal bilesenleri kapsar, zorlu saha kosullarina dayanacak sekilde imal edilir.",
               "applications": "Bu parcalar; insaat, yikim ve toprak isleri boyunca ekskavator, kaydirmali yukleyici ve loader uzerinde kullanilir."},
        "fr": {"what_is": "Les pièces de construction et d'excavatrice couvrent les accessoires en acier lourd et les composants structurels pour les engins de chantier, y compris les godets, fourches et éléments de flèche, fabriqués pour résister aux conditions de chantier exigeantes.",
               "applications": "Ces pièces sont utilisées sur les excavatrices, chargeuses compactes et chargeuses, dans les travaux de construction, de démolition et de terrassement."},
        "ar": {"what_is": "تشمل قطع غيار البناء والحفارات ملحقات فولاذية ثقيلة ومكونات إنشائية لآلات البناء، بما في ذلك الجرافات والشوك ومكونات الذراع، مصنعة لتحمل ظروف الموقع الصعبة.",
               "applications": "تُستخدم هذه القطع على الحفارات والشاحنات الانزلاقية والمحملات في أعمال البناء والهدم وأعمال الحفر."},
    },
}

PRODUCT_DETAIL_UI = {
    "en": {"what_is": "What is {name}?", "applications": "Typical Applications", "back": "All Products",
           "cta_p": "Need exact dimensions, grade, or a price for {name}? Send us your specs and we'll get back with a quote.",
           "cta_btn": "Get a Quote"},
    "tr": {"what_is": "{name} Nedir?", "applications": "Tipik Kullanim Alanlari", "back": "Tum Urunler",
           "cta_p": "{name} icin tam olcu, kalite veya fiyat mi lazim? Ozelliklerinizi gonderin, teklifle donus yapalim.",
           "cta_btn": "Teklif Al"},
    "fr": {"what_is": "Qu'est-ce que {name} ?", "applications": "Applications Typiques", "back": "Tous les Produits",
           "cta_p": "Besoin de dimensions exactes, d'une nuance ou d'un prix pour {name} ? Envoyez-nous vos spécifications, nous reviendrons avec un devis.",
           "cta_btn": "Demander un devis"},
    "ar": {"what_is": "ما هو {name}؟", "applications": "الاستخدامات الشائعة", "back": "جميع المنتجات",
           "cta_p": "هل تحتاج إلى أبعاد أو نوع أو سعر دقيق لـ {name}؟ أرسل لنا التفاصيل وسنرد بعرض سعر.",
           "cta_btn": "اطلب عرض سعر"},
}

def product_slug(key):
    return key.replace("_", "-")

GALLERY_EXTRA = {
    "constr_bucket_black": ["constr_bucket_grey1", "constr_bucket_grey2", "constr_forks", "constr_arm", "constr_bucket_yellow"],
}

def product_detail_body(key, name, native, category_label, category_href, img_key, lang="en"):
    info = PRODUCT_INFO[key][lang]
    U = PRODUCT_DETAIL_UI[lang]
    extra_keys = GALLERY_EXTRA.get(key, [])
    gallery_html = ""
    if extra_keys:
        thumbs = "\n".join([
            f'<div class="thumb" style="background-image:url(\'{PRODUCT_B64[k]}\')"></div>'
            for k in extra_keys
        ])
        gallery_html = f'<div class="product-gallery-grid">{thumbs}</div>'
    return f"""
<section class="banner" style="background-image:url('{PRODUCT_B64[key]}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">{name}</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap service-detail-grid reveal">
    <div class="service-detail-main">
      <div class="service-detail-hero" style="background-image:url('{PRODUCT_B64[key]}')"></div>
      <p style="color:var(--coral); font-family:'Poppins'; font-size:12px; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:10px;">{native}</p>
      <h3>{U['what_is'].format(name=name)}</h3>
      <p>{info['what_is']}</p>
      <h3>{U['applications']}</h3>
      <p>{info['applications']}</p>
      {gallery_html}
    </div>
    <div>
      <div class="service-sidebar">
        <h4>{category_label}</h4>
        <a href="{category_href}">{U['back']}</a>
      </div>
      <div class="service-detail-cta">
        <p>{U['cta_p'].format(name=name)}</p>
        <a class="more" href="contact.html">{U['cta_btn']}</a>
      </div>
    </div>
  </div>
</section>
"""
FR_PRODUCT_NAMES = {
    "kutu_profil": "Profil\u00e9 Carr\u00e9", "metal_boru": "Tube M\u00e9tallique", "kosebent": "Corni\u00e8re",
    "lama_demiri": "Fer Plat", "silme_demiri": "Fer Silme",
    "npu_demiri": "Poutrelles (NPU/NPI/IPE/HEA/HEB)", "kare_demir": "Fer Carr\u00e9", "t_demir": "Fer en T",
    "transmisyon_mili": "Arbre de Transmission", "sac_cesitleri": "T\u00f4le",
    "cati_panelleri": "Panneaux de Toiture", "cephe_panelleri": "Panneaux de Fa\u00e7ade",
    "imalat_celigi": "Acier de Construction", "islah_celigi": "Acier Tremp\u00e9",
    "otomat_celigi": "Acier de D\u00e9colletage", "sementasyon_celigi": "Acier de C\u00e9mentation",
    "pas_sac_levha": "T\u00f4le Inox", "pas_profil": "Profil\u00e9 Inox", "pas_lama": "Fer Plat Inox",
    "pas_altikose": "Barre Hexagonale Inox", "pas_dikisli_boru": "Tube Inox Soud\u00e9",
    "pas_dikissiz_boru": "Tube Inox Sans Soudure", "pas_cubuk_mil": "Barre Ronde Inox (Arbre)",
    "pas_fittings": "Raccords Inox",
    "shredder_knives": "Lames de Broyeur de Recyclage",
    "constr_bucket_black": "Pièces de Construction et d'Excavatrice",
}

AR_PRODUCT_NAMES = {
    "kutu_profil": "قوطي مربع", "metal_boru": "أنبوب معدني", "kosebent": "زاوية حديد",
    "lama_demiri": "حديد لامة", "silme_demiri": "حديد سلمة",
    "npu_demiri": "كمرات إنشائية (NPU/NPI/IPE/HEA/HEB)", "kare_demir": "حديد مربع", "t_demir": "حديد T",
    "transmisyon_mili": "عمود نقل الحركة", "sac_cesitleri": "أنواع الصاج",
    "cati_panelleri": "ألواح أسقف", "cephe_panelleri": "ألواح واجهات",
    "imalat_celigi": "صلب التصنيع", "islah_celigi": "صلب مقسّى",
    "otomat_celigi": "صلب سريع التشغيل", "sementasyon_celigi": "صلب مُسمّن",
    "pas_sac_levha": "صاج ستانلس ستيل", "pas_profil": "بروفايل ستانلس ستيل", "pas_lama": "لامة ستانلس ستيل",
    "pas_altikose": "سداسي ستانلس ستيل", "pas_dikisli_boru": "أنبوب ستانلس ملحوم",
    "pas_dikissiz_boru": "أنبوب ستانلس سلس", "pas_cubuk_mil": "عمود ستانلس مستدير",
    "pas_fittings": "وصلات ستانلس ستيل",
    "shredder_knives": "شفرات آلة تقطيع إعادة التدوير",
    "constr_bucket_black": "قطع غيار البناء والحفارات",
}

PROD_UI = {"en": "Product Lines", "tr": "\u00dcr\u00fcn Gruplar\u0131", "fr": "Gammes de Produits", "ar": "فئات المنتجات"}

def product_display_name(key, en, native, lang):
    if lang == "en": return en
    if lang == "tr": return native
    if lang == "fr": return FR_PRODUCT_NAMES[key]
    if lang == "ar": return AR_PRODUCT_NAMES[key]
    return en

def product_gallery_body(banner_title, section_title, items, img_key, lang="en"):
    cards = "\n".join([
        f"""<a class="product-cat-card" href="{product_slug(key)}.html">
      <div class="thumb" style="background-image:url('{PRODUCT_B64[key]}')"></div>
      <div class="body">
        <span class="native-name">{native if lang != "tr" else en}</span>
        <h3>{product_display_name(key, en, native, lang)}</h3>
      </div>
    </a>""" for key, en, native in items
    ])
    return f"""
<section class="banner" style="background-image:url('{IMG_B64[img_key]}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">{banner_title}</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">{PROD_UI[lang]}</span>
    <h2 class="section-title">{section_title}</h2>
  </div>
  <div class="product-cat-grid reveal-stagger">
    {cards}
  </div>
</section>
"""

demir_body = product_gallery_body("Iron &amp; Steel Products", "Iron and steel products, by category.", demir_items, "profile")
open(f"{EN_OUT_DIR}/demir-celik-urunler.html","w").write(page("Iron &amp; Steel Products","demir",demir_body,slug="demir-celik-urunler"))

paslanmaz_body = product_gallery_body("Stainless Steel Products", "Stainless steel products, by category.", paslanmaz_items, "sheet")
open(f"{EN_OUT_DIR}/paslanmaz-urunler.html","w").write(page("Stainless Steel Products","paslanmaz",paslanmaz_body,slug="paslanmaz-urunler"))

for key, name, native in demir_items + paslanmaz_items:
    is_demir = (key, name, native) in demir_items
    cat_href = "demir-celik-urunler.html" if is_demir else "paslanmaz-urunler.html"
    cat_label = NAV_LABELS["en"]["demir"] if is_demir else NAV_LABELS["en"]["paslanmaz"]
    body = product_detail_body(key, name, native, cat_label, cat_href, "profile" if is_demir else "sheet", lang="en")
    desc = PRODUCT_INFO[key]["en"]["what_is"][:160]
    open(f"{EN_OUT_DIR}/{product_slug(key)}.html","w").write(page(name, "demir" if is_demir else "paslanmaz", body, slug=product_slug(key), description=desc))

# ---------------- SERVICE DETAIL PAGES ----------------
service_details = [
    {
        "slug": "iron-steel-supply", "title": "Iron &amp; Steel Supply", "img": "bars",
        "intro": "Alongside our cutting, bending, and fabrication services, Nora Paslanmaz ve Celik supplies a wide range of iron and steel products directly, sheet, profile, pipe, rolled stock, and steel mesh among them, manufactured on modern equipment and backed by our own quality guarantee.",
        "what_is": "Our production facility is built for high volume and supported by up-to-date technology, which lets us take on custom orders alongside standard stock. Beyond supplying finished material, we also offer related processing on request, including profile cutting, pipe cutting, sheet cutting, sheet bending, and coil slitting, so a single order can cover both raw material and the shaping it needs.",
        "methods": "We source and supply materials for a wide range of downstream products, backed by competitive pricing, consistent quality, on-time delivery, and dependable after-sales support, and we deliver anywhere in Turkey on the schedule you need. Nora Paslanmaz ve Celik works on a customer-first basis, reach out to our team directly for stock availability, technical questions, or a quote before you decide.",
    },
    {
        "slug": "cutting-bending", "title": "Cutting and Bending", "img": "cutbend",
        "intro": "On our CNC press brakes, we bend sheet metal of varying thicknesses and dimensions with precision, meeting the forming needs of a wide range of industries. Our experienced team combines material expertise with high-technology CNC bending equipment to complete even the most complex sheet-forming jobs quickly and accurately.",
        "what_is": "Cutting and bending is an industry built around shaping sheet and metal stock into the profiles a project actually needs, whether flat plate, angle sections, or channel forms used across the automotive and construction industries, among others. Because it is the first stage in so much downstream production, getting this step right, on time and to the requested dimensions, matters for everything that follows.",
        "methods": "Our press brakes span a range of tonnages and working widths, each combining an upper die, lower die, hydraulic axes, and a CNC control unit, hydraulic pressure clamps the sheet between matched V-shaped dies to form each bend to the programmed angle. Material type, thickness, and required pressure are set through the CNC system before forming begins, keeping every bend fast, accurate, and repeatable. Nora Paslanmaz ve Celik combines cutting and bending with our laser cutting and welding services for a single continuous production workflow, with support available around the clock for questions or new orders.",
    },
    {
        "slug": "cnc-machining", "title": "CNC Machining", "img": "cnc",
        "intro": "CNC machining covers turning, milling, drilling, and grinding processes that remove material from a workpiece in thin layers to bring it to an exact final shape, size, and surface finish. It has been central to industrial manufacturing since the 20th century and remains essential wherever precise dimensions matter.",
        "what_is": "In CNC (Computer Numerical Control) machining, cutting tools guided by a digital program remove material from a workpiece, whether by turning, milling, or drilling, until it reaches the exact dimensions of the design. Compared to manual methods, CNC machines complete this work faster and more safely, which is also why they are widely used across the furniture and industrial fabrication sectors.",
        "methods": "CNC machining suits a wide range of materials and finishes, holding tight dimensional tolerances and producing clean, finished surfaces, with parts easily reworked to a different size or shape whenever needed. The one tradeoff is a small amount of material lost as offcuts during shaping, whether the material is metal, plastic, or timber, a normal and expected part of the process. Nora Paslanmaz ve Celik offers a full range of CNC turning, milling, and grinding equipment backed by warranty terms and an experienced team on hand to advise on the right machine for your job.",
    },
    {
        "slug": "welded-fabrication", "title": "Welded Fabrication", "img": "welded_fab",
        "intro": "Welded fabrication joins individual components, in stainless steel, iron, aluminum, and other metals, into a single structurally sound assembly. It is one of the most widely relied-upon manufacturing methods worldwide, and critical across a wide range of industries.",
        "what_is": "Welded fabrication is chosen because it delivers low-error, high-efficiency results at a lower cost than many alternative joining methods, and advances in automation have made it adaptable to nearly every industry and material combination. The right welding method still has to be matched to the material being joined, which is why our experienced team plans each project around the technique and equipment best suited to it, keeping production efficient and cost-effective.",
        "methods": "Because welded fabrication rewards careful planning, we analyze every project in detail before work begins, from logistics through weld sequencing, to keep scrap rates low and hold the finished assembly to its agreed delivery schedule. Nora Paslanmaz ve Celik manages this process end to end, from small custom brackets to structural work for buildings, bridges, and piping systems, backed by an experienced team and technical support whenever your project needs it.",
    },
    {
        "slug": "plasma-cutting", "title": "Plasma Cutting", "img": "plasma",
        "intro": "Plasma cutting uses a high-velocity jet of ionized gas, delivered through a narrow nozzle, to heat and cut through electrically conductive metal. It is one of the fastest methods available for cutting steel and other structural material, and performs especially well on non-alloy steels and heavier-gauge sheet.",
        "what_is": "In plasma cutting, ionized gas is forced through a narrow nozzle at high speed and temperature, carrying an electrical current that heats and melts the metal on contact, while the high-speed gas jet blows the molten material clear of the cut. It is recommended by industry specialists for cutting steel and non-ferrous metals up to around 25mm thick, including special cases, such as mesh-form metals, that oxy-fuel cutting cannot handle well.",
        "methods": "Compared to purely mechanical cutting methods, plasma delivers noticeably faster results and handles non-flat or irregular cuts with ease. It works on any electrically conductive metal, and its technology also allows precise grooving within the same cutting pass. By nesting multiple parts on the same sheet, scrap is kept to a minimum, and the process itself produces a near burr-free edge with minimal heat distortion, even through material roughly 1.5 times the sheet thickness. Nora Paslanmaz ve Celik applies plasma cutting for fast, accurate results at competitive prices, including surface engraving of emblems or artwork on request.",
    },
    {
        "slug": "laser-cutting", "title": "Laser Cutting", "img": "laser",
        "intro": "Laser cutting uses a high-powered, precisely focused beam of light to cut sheet metal, producing clean, smooth edges with very little post-processing. It is one of the most widely used cutting methods in industrial manufacturing, valued for the quality of cut it produces.",
        "what_is": "In laser cutting, a high-powered, focused beam of light is guided by an automated system across stainless steel, iron, aluminum, and other sheet metals, cutting them into the required shape. Even complex geometries that would normally take days can be completed in as little as 24 hours, since the beam follows the cutting path directly from the digital design file.",
        "methods": "Because the process is computer-guided from the original design, laser cutting reduces both material waste and tooling costs compared to conventional cutting, cutting down on the jigs and dies older methods require. It stays highly accurate even at high output, with human error kept to a minimum despite the intensity of the process. Nora Paslanmaz ve Celik uses laser cutting on stainless steel, iron, aluminum, and other metal sheets, delivering precise, competitively priced results for every job, from single custom parts to full production runs.",
    },
]

SVC_UI = {
    "en": {"nedir": "What is {title}?", "methods": "Methods and Advantages",
           "sidebar_h": "Services", "cta_p": "Have a project in mind? Send us your specs and we'll get back with pricing and lead time.",
           "cta_btn": "Get a Quote"},
    "tr": {"nedir": "{title} Nedir?", "methods": "Y\u00f6ntemler ve Avantajlar",
           "sidebar_h": "Hizmetler", "cta_p": "Bir projeniz mi var? Ozelliklerinizi bize g\u00f6nderin, fiyat ve teslim s\u00fcresi ile d\u00f6n\u00fc\u015f yapal\u0131m.",
           "cta_btn": "Teklif Al"},
    "fr": {"nedir": "Qu'est-ce que {title} ?", "methods": "M\u00e9thodes et avantages",
           "sidebar_h": "Services", "cta_p": "Vous avez un projet en t\u00eate ? Envoyez-nous vos sp\u00e9cifications, nous reviendrons vers vous avec un prix et un d\u00e9lai.",
           "cta_btn": "Demander un devis"},
    "ar": {"nedir": "ما هي {title}؟", "methods": "الطرق والمزايا",
           "sidebar_h": "الخدمات", "cta_p": "هل لديك مشروع؟ أرسل لنا تفاصيله وسنعاود التواصل معك بعرض سعر وموعد تسليم.",
           "cta_btn": "اطلب عرض سعر"},
}

def service_detail_body(svc, all_services, lang="en"):
    U = SVC_UI[lang]
    sidebar_links = "\n".join([
        f'<a href="{s["slug"]}.html" class="{"active" if s["slug"]==svc["slug"] else ""}">{s["title"]}</a>'
        for s in all_services
    ])
    return f"""
<section class="banner" style="background-image:url('{IMG_B64[svc['img']]}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">{svc['title']}</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap service-detail-grid reveal">
    <div class="service-detail-main">
      <div class="service-detail-hero" style="background-image:url('{IMG_B64[svc['img']]}')"></div>
      <p>{svc['intro']}</p>
      <h3>{U['nedir'].format(title=svc['title'])}</h3>
      <p>{svc['what_is']}</p>
      <h3>{U['methods']}</h3>
      <p>{svc['methods']}</p>
    </div>
    <div>
      <div class="service-sidebar">
        <h4>{U['sidebar_h']}</h4>
        {sidebar_links}
      </div>
      <div class="service-detail-cta">
        <p>{U['cta_p']}</p>
        <a class="more" href="contact.html">{U['cta_btn']}</a>
      </div>
    </div>
  </div>
</section>
"""

for svc in service_details:
    body = service_detail_body(svc, service_details)
    open(f"{EN_OUT_DIR}/{svc['slug']}.html","w").write(page(svc['title'],"services",body,slug=svc['slug'],svc=svc))

# ---------------- ABOUT ----------------
about_body = f"""
<section class="banner" style="background-image:url('{BANNER_IMAGES['about_building']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">About Us</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap about-grid reveal">
    <div>
      <span class="section-eyebrow">Who We Are</span>
      <h2 class="section-title" style="margin-bottom:20px;">Manufacturing partner for stainless and steel.</h2>
      <p>With years of experience in the iron, steel, and stainless steel industry, Nora Paslanmaz ve Celik serves its customers through expertise, service quality, and competitively priced products. Nora has earned its place among the leading companies in the sector, a position we take rightful pride in.</p>
      <p>Guided by a customer-first philosophy, our company stays true to its commitment to quality through continuous research, development, and adherence to global quality standards, establishing itself as a distinguished name in the industry.</p>
      <p>Nora Paslanmaz ve Celik carries out every aspect of its operations with an experienced and skilled team, working at full capacity before and after every sale to ensure our valued customers are never left without support.</p>
      <div class="about-stats">
        <div class="stat"><b>6</b><span>Core Processes</span></div>
        <div class="stat"><b>TR</b><span>Istanbul Based</span></div>
        <div class="stat"><b>B2B</b><span>Direct Supply</span></div>
      </div>
      <a class="more about-download" href="../nora-company-profile.pdf" download="Nora-Company-Profile.pdf">Download Company Profile</a>
    </div>
    <div class="about-visual" style="background-image:url('{IMG_B64['welded_fab']}'); background-size:cover; background-position:center;"></div>
  </div>
</section>
"""
open(f"{EN_OUT_DIR}/about.html","w").write(page("About Us","about",about_body,slug="about"))

# ---------------- CERTIFICATES ----------------
certificates_body = f"""
<section class="banner" style="background-image:url('{IMG_B64['cnc']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Certificates</h2></div></section>
<section class="partners" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">Certificates &amp; References</span>
    <h2 class="section-title" style="margin-bottom:40px;">Trusted by industry partners.</h2>
  </div>
  <div class="wrap">
  <div class="cert-grid reveal-stagger">
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso9001']}" alt="ISO 9001:2015"><p>ISO 9001:2015<br>Quality Management</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso10002']}" alt="ISO 10002:2018"><p>ISO 10002:2018<br>Customer Satisfaction</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso14001']}" alt="ISO 14001:2015"><p>ISO 14001:2015<br>Environmental Management</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso45001']}" alt="ISO 45001:2018"><p>ISO 45001:2018<br>Occupational Health &amp; Safety</p></div>
  </div>
  </div>
</section>
"""
open(f"{EN_OUT_DIR}/certificates.html","w").write(page("Certificates","certificates",certificates_body,slug="certificates"))

blog_posts = [
    {
        "slug": "iron-steel-products-explained", "title": "Iron &amp; Steel Products", "img": "profile",
        "category": "Products",
        "excerpt": "Steel is an alloy of iron and carbon, and the carbon ratio shapes everything from classification to hardness. A look at our range and where each product is used.",
        "paragraphs": [
            ("", "Steel is an alloy made from a combination of iron and carbon, typically ranging between 0.2% and 2.1% carbon content. The carbon content plays a key role in how steel is classified. Iron produced in blast furnaces is converted into steel either through a series of refining processes or by remelting scrap in electric arc furnaces. Carbon is the element that hardens iron, the higher the carbon ratio in the resulting mix, the harder the steel becomes. At Nora Paslanmaz ve Celik, we supply our customers with the highest quality iron and steel products."),
            ("What Are Iron &amp; Steel Products?", "Iron and steel products come in a wide range of forms. Among what we supply are NPU profiles, angle sections, black sheet, transmission shafts, cold-rolled (DKP) sheet, K-profile, rebar, coated K-profile, flat bar, NPI profiles, square bar, ribbed bar, checkered plate, galvanized sheet, galvanized trapezoidal sheet, galvanized square profile, expanded metal sheet, and galvanized or black water pipe, simply get in touch with our team for any of these. Our specialized staff and modern machinery are what set us apart in iron and steel products."),
            ("Sheet", "Sheet metal is one of the most basic needs across industrial manufacturing, used in different forms across different applications. A sheet metal supplier needs to be able to offer cutting tailored to your specifications, and that is exactly what we provide. Sheet also offers a number of practical advantages, material that supports serial production can lower your overall production costs. Sheet dimensions and pricing vary depending on the specification you choose, with pricing set according to the product's technical properties. Below a certain volume, sheet can be produced without requiring a die at all, keeping material deformation close to zero."),
            ("Profiles", "Because different metals come in different thicknesses and grades, the machinery used to cut them varies accordingly, no single method works for every material. Cut sections are cleaned before further processing, a step that ensures no residue is left on the steel, which is essential for achieving the precise contour cuts the work requires. We carry out every step needed to keep profile-cutting lead times short, and deliver the finished product ready for assembly or further machining. Oxygen, plasma, and laser cutters are the machines we use for profile cutting."),
            ("Where Are Iron &amp; Steel Products Used?", "Iron and steel products are chosen across a wide range of industries, in decoration, for decorative fittings, in automotive, for vehicle underbody structures, in construction, in furniture, for legs and arm frames, in textiles, for hangers, mannequins, and weaving looms, in electronics, for computer and equipment housings, and in shipbuilding and heavy industry. We supply iron and steel products across all of these applications. Since the day we were founded, our company has built a name for professionalism and quality, and we continue producing the best possible products for our customers."),
        ],
    },
    {
        "slug": "stainless-steel-products-explained", "title": "Stainless Steel Products", "img": "sheet",
        "category": "Products",
        "excerpt": "Stainless steel is created by adding chromium to steel in specific proportions. A look at where it offers an advantage, how it's priced, and how to store it correctly.",
        "paragraphs": [
            ("", "Stainless steel is an alloy created by adding a specific proportion of chromium to steel, and it is one of the most widely chosen materials in manufacturing today. Because of the many advantages it offers in production, demand for stainless steel keeps growing year after year. At Nora Paslanmaz Celik, we have spent years keeping the stainless steel products our industry needs in stock, supplying you without disrupting your production. Our technical staff are available for product information and technical support on any order you place with us."),
            ("Where Stainless Steel Offers an Advantage", "<em>[Editorial note for Andi: the client's screenshots skip a short section here, likely one photo/scroll position. The paragraph below is a general placeholder bridging the gap, please swap it out once the missing part is sent.]</em> Stainless steel brings a distinct set of advantages to production, particularly its resistance to corrosion and its consistency across repeated production runs, allowing manufacturing to continue without loss of quality. Stainless steel itself can be divided into different types and grades. Because these differences exist within stainless steel, sourcing your material from a reliable supplier keeps the problems they can cause in production to a minimum. By quality standard, stainless steel is a product that increases resistance to corrosion. Alongside these differences, weldability, machinability, heat-treatability, and mechanical properties can all vary as well. Some stainless steel grades, for example, contain less carbon and are more elastic as a result, which can create challenges during processing. We provide detailed guidance on the right stainless steel product for your intended use before any work begins.<br><br>Despite its name, stainless steel is not stain-proof under all circumstances, that depends on using the correct stainless alloy in the correct production process. Stainless steel keeps its stain-resistant properties when used in the conditions it is suited for, and loses them otherwise. For all these reasons, it matters where you source your stainless steel from. Our knowledgeable, well-trained team at Nora Paslanmaz Celik is here to provide you with quality service on every product."),
            ("Stainless Steel Pricing", "Stainless steel pricing can vary with market conditions. While price is an important factor when buying stainless steel, what matters most is finding the right grade for your production. Choosing correctly means the parts made from it will hold up over the long term without issue. When buying stainless steel, pay attention to its corrosion resistance, mechanical strength, the temperatures your production process involves, and its physical and surface properties. We provide the technical support you need on all of these points as part of every sale."),
            ("How Should Stainless Steel Be Stored?", "Where you store stainless steel affects whether the product stays free of deformation. Storage areas should keep it off direct contact with soil, and away from carbon steel shavings stored in the same space. If these precautions are not followed, stainless steel's properties can be compromised and signs of rust can appear on the product."),
        ],
    },
]

BLOG_UI = {
    "en": {"categories": "Categories", "all": "All Categories",
           "cta_p": "Have a project in mind? Send us your specs and we'll get back with pricing and lead time.", "cta_btn": "Get a Quote"},
    "tr": {"categories": "Kategoriler", "all": "T\u00fcm Kategoriler",
           "cta_p": "Bir projeniz mi var? Ozelliklerinizi bize g\u00f6nderin, fiyat ve teslim s\u00fcresi ile d\u00f6n\u00fc\u015f yapal\u0131m.", "cta_btn": "Teklif Al"},
    "fr": {"categories": "Cat\u00e9gories", "all": "Toutes les cat\u00e9gories",
           "cta_p": "Vous avez un projet en t\u00eate ? Envoyez-nous vos sp\u00e9cifications, nous reviendrons vers vous avec un prix et un d\u00e9lai.", "cta_btn": "Demander un devis"},
    "ar": {"categories": "الفئات", "all": "جميع الفئات",
           "cta_p": "هل لديك مشروع؟ أرسل لنا تفاصيله وسنعاود التواصل معك بعرض سعر وموعد تسليم.", "cta_btn": "اطلب عرض سعر"},
}

def blog_detail_body(post, all_posts, lang="en"):
    U = BLOG_UI[lang]
    other_links = "\n".join([
        f'<a href="{p["slug"]}.html" class="{"active" if p["slug"]==post["slug"] else ""}">{p["title"]}</a>'
        for p in all_posts
    ])
    body_html = "\n".join([
        (f'<h3>{h}</h3>\n<p>{p}</p>' if h else f'<p>{p}</p>')
        for h, p in post["paragraphs"]
    ])
    return f"""
<section class="banner" style="background-image:url('{IMG_B64[post['img']]}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">{post['title']}</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap service-detail-grid reveal">
    <div class="service-detail-main">
      <div class="service-detail-hero" style="background-image:url('{IMG_B64[post['img']]}')"></div>
      {body_html}
    </div>
    <div>
      <div class="service-sidebar">
        <h4>{U['categories']}</h4>
        <a href="blog.html" class="">{U['all']}</a>
        {other_links}
      </div>
      <div class="service-detail-cta">
        <p>{U['cta_p']}</p>
        <a class="more" href="contact.html">{U['cta_btn']}</a>
      </div>
    </div>
  </div>
</section>
"""

for post in blog_posts:
    body = blog_detail_body(post, blog_posts)
    open(f"{EN_OUT_DIR}/{post['slug']}.html","w").write(page(post['title'],"blog",body,slug=post['slug']))

# ---------------- BLOG ----------------
blog_cards = "\n".join([f"""
    <div class="blog-card">
      <div class="thumb" style="background-image:url('{IMG_B64[p['img']]}'); background-size:cover; background-position:center;"></div>
      <div class="body">
        <span class="date">{p['category']}</span>
        <h3>{p['title']}</h3>
        <p>{p['excerpt']}</p>
        <a class="more" href="{p['slug']}.html">Read More</a>
      </div>
    </div>""" for p in blog_posts])

blog_body = f"""
<section class="banner" style="background-image:url('{IMG_B64['bars']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Blog</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">News &amp; Updates</span>
    <h2 class="section-title">Latest from Nora.</h2>
  </div>
  <div class="wrap">
  <div class="blog-grid reveal-stagger">{blog_cards}
  </div>
  </div>
</section>
"""
open(f"{EN_OUT_DIR}/blog.html","w").write(page("Blog","blog",blog_body,slug="blog"))

# ---------------- CONTACT ----------------
contact_body = f"""
<section class="banner" style="background-image:url('{BANNER_IMAGES['contact_gate']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Contact</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap contact-grid reveal">
    <div>
      <span class="section-eyebrow">Get in Touch</span>
      <h2 class="section-title">Request a quote.</h2>
      <ul class="contact-list">
        <li><b>Phone</b> 0216 621 55 41</li>
        <li><b>Email</b> info@norapaslanmazglobal.com</li>
        <li><b>Address</b> OSB Des Sanayi Sitesi 115 Sok. No:30, Yukari Dudullu, Umraniye / Istanbul</li>
      </ul>
    </div>
    <div class="form-box">
      <form class="ajax-form" data-success="Thanks, your inquiry has been sent. We'll get back to you shortly." data-error="Something went wrong. Please try again or call us directly.">
        <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
        <input type="hidden" name="subject" value="New Quote Request - Nora Website">
        <input type="checkbox" name="botcheck" style="display:none">
        <div class="form-row"><label>Full Name</label><input type="text" name="name" placeholder="Your name" required></div>
        <div class="form-row"><label>Email</label><input type="email" name="email" placeholder="you@company.com" required></div>
        <div class="form-row"><label>Company</label><input type="text" name="company" placeholder="Company name"></div>
        <div class="form-row"><label>Message</label><textarea name="message" placeholder="Quantity, dimensions, and any specs..." required></textarea></div>
        <button type="submit" class="submit-btn">Send Inquiry</button>
        <p class="form-status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
<section style="padding:0 60px 90px;">
  <div class="map-frame">
    <iframe
      src="https://www.google.com/maps?q=DES+Sanayi+Sitesi,+Nato+Yolu+Cd,+Yukar%C4%B1+Dudullu,+%C3%9Cmraniye%2F%C4%B0stanbul&output=embed"
      width="100%" height="420" style="border:0;" allowfullscreen="" loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>
"""
open(f"{EN_OUT_DIR}/contact.html","w").write(page("Contact","contact",contact_body,slug="contact"))

open("/home/claude/nora-site/pages/style.css","w").write(STYLE)
open("/home/claude/nora-site/pages/script.js","w").write(SHARED_SCRIPT_BASE.split("<script>\n",1)[1])

# ================= TURKISH (TR) VERSION =================
TR_OUT_DIR = "/home/claude/nora-site/pages"
os.makedirs(TR_OUT_DIR, exist_ok=True)

def write_tr(slug, title, current, body, extra_script="", svc=None, description=None):
    open(f"{TR_OUT_DIR}/{slug}.html", "w").write(page(title, current, body, extra_script, lang="tr", slug=slug, svc=svc, description=description))

# ---------------- TR: HERO ----------------
HERO_SLIDES_TR = [
    ("Hizmet / 01", "CNC Kesim", "cnc", "services.html"),
    ("Hizmet / 02", "Lazer Kesim", "laser", "services.html"),
    ("Hizmet / 03", "Plazma Kesim", "plasma", "services.html"),
    ("Hizmet / 04", "Kaynakli Imalat", "welded_fab", "services.html"),
    ("Hizmet / 05", "Kesim Bukum", "cutbend", "services.html"),
    ("Urunler", "Boru, Profil ve Celik", "pipes", "demir-celik-urunler.html"),
]
HERO_SCRIPT_TR = hero_script(HERO_SLIDES_TR)

home_body_tr = f"""
<div class="hero-spacer" id="heroSpacer"></div>
<div class="hero-fixed" id="heroFixed">
  <div class="hero-viewport">
    <div class="hero-track" id="heroTrack"></div>
  </div>
  <div class="slide-label" id="slideLabel">
    <div class="slide-eyebrow" id="labelEyebrow">Hizmet / 01</div>
    <h1 id="labelTitle">CNC Kesim</h1>
    <div class="slide-rule"></div>
  </div>
  <div class="scroll-hint" id="scrollHint"><div class="line"></div>SCROLL</div>
</div>
<section class="home-highlights">
  <div class="wrap">
    <div class="hl-grid reveal">
      <div class="hl-intro">
        <span class="section-eyebrow">Nora Hakkinda</span>
        <h2 class="section-title" style="margin-bottom:20px;">Paslanmaz ve celik icin uretim ortaginiz.</h2>
        <p>Demir, celik ve paslanmaz celik sektorundeki yillarin deneyimiyle Nora Paslanmaz ve Celik, uzmanlik, hizmet kalitesi ve rekabetci fiyatli urunler ile musterilerine hizmet vermektedir. Musteri odakli felsefemizle kuresel kalite standartlarina bagli kaliyoruz.</p>
        <a class="more hl-download" href="nora-company-profile.pdf" download="Nora-Sirket-Profili.pdf">Sirket Profilini Indir</a>
      </div>
      <div class="hl-certs">
        <span class="section-eyebrow">Sertifikali</span>
        <div class="hl-cert-grid">
          <img src="{CERT_IMAGES['cert_iso9001']}" alt="ISO 9001:2015">
          <img src="{CERT_IMAGES['cert_iso14001']}" alt="ISO 14001:2015">
          <img src="{CERT_IMAGES['cert_iso45001']}" alt="ISO 45001:2018">
          <img src="{CERT_IMAGES['cert_iso10002']}" alt="ISO 10002:2018">
        </div>
        <a class="more" href="certificates.html">Tum Sertifikalar</a>
      </div>
    </div>
    <div class="hl-cta reveal">
      <h3>Projeniz hakkinda konusmaya hazir misiniz?</h3>
      <a class="more" href="contact.html">Teklif Isteyin</a>
    </div>
  </div>
</section>
"""
write_tr("index", "Anasayfa", "home", home_body_tr, HERO_SCRIPT_TR)

# ---------------- TR: SERVICES ----------------
service_details_tr = [
    {
        "slug": "iron-steel-supply", "title": "Demir Celik Urun", "img": "bars",
        "intro": "Firmamiz bunyesinde demir celik urunler uretimi esnasinda son teknoloji cihazlar kullanildigindan urunlerde hata, sorun cikmasi muhtemel degildir. Istenilen ozelliklere uygun olarak birebir ayni urunlerin satislari yapilmaktadir. Urunlerimiz firmamiz guvencesi ile satisa sunulmaktadir. Saclar, profiller, borular, hadde urunleri, celik hasirlar, demir celik urunler bunlardan bazilaridir.",
        "what_is": "Genis uretim hacmine sahip olan firmamiz yeni nesil teknolojiler ile desteklenen bir uretim alanina sahiptir. Ihtiyaclariniza ozel cozumler sunmak icin ozel uretimler gerceklestirmekteyiz. Demir celik urun satisi konusunda sektorun en iyi fiyatlandirmasini sizlere sunan firmamizdan teklif almadan karar vermeyin. Profil kesim, boru kesim, sac kesim, sac bukum, rulo dilme kesim ve rulo sac kesim gibi hizmetleri de sunmaktayiz.",
        "methods": "Firmamiz hayatimizda az ya da cok kullandigimiz pek cok urun icin malzeme tedariki saglamaktadir. En kaliteli demir celik urunlerini uygun fiyat garantisi ile sizlere sunan firmamiz yuzde yuz musteri odakli calisan bir firma olmakla birlikte kaliteli, zamaninda teslimat ve satis sonrasi hizmetler konusunda oldukca titiz calismaktadir. Turkiye'nin her yerine istenilen gunde teslim edilecek demir celik urunler icin hemen simdi arayabilirsiniz.",
    },
    {
        "slug": "cutting-bending", "title": "Kesim Bukum", "img": "cutbend",
        "intro": "Nora Paslanmaz ve Celik Firmasi olarak CNC tezgahlarimizda, muhtelif olcu ve kalinliklarda bulunan saclari buyuk bir itina ile bukerek, farkli sektorlerdeki ihtiyaclarinizi karsilamaktayiz. Firmamiz yuksek teknolojili CNC Bukum Tezgahlarinda, malzeme bilgisi ve teknik altyapiya sahip deneyimli kadromuz ile en karmasik sac bukum islerini dahi hatasiz ve en hizli sekilde gerceklestirerek sizlere sunmaktayiz.",
        "what_is": "Kesim bukum, gunumuzde sac ve metal uzerine kurulu bir sanayidir. Bu alan her gecen gun gelismektedir. Birçok urun artik bu malzemelerin islenmesi ile ortaya cikmaktadir. Ileri teknoloji makineler kullanarak bu alanda kendisini gelistiren firmamiz ile calisirsaniz zamaninda istediginiz gibi bir teslimat almaniz mumkundur. Firmamiz ileri teknolojik alt yapisi ile Turkiye'nin her yerine hizmet verebilmektedir.",
        "methods": "Farkli tonajlarda ve genisliklerde kesim bukum cihazlarimiz mevcuttur. Ust kalip, alt kalip, hidrolik eksenleri, CNC kontrol unitesi gibi siniflardan olusmaktadir. Malzeme turu, malzeme kalinliklari ve uygulanacak basinc gibi ozelliklere gore son teknolojik kesme bukum cihazlarina girilir ardindan islemler baslamaktadir. Diledginiz urunu en kisa surede size teslim edecek, lazer kesim, ileri kesim bukum ve diger islemler icin hemen firmamiz ile baglanti kurabilirsiniz.",
    },
    {
        "slug": "cnc-machining", "title": "Talasli Imalat", "img": "cnc",
        "intro": "Talasli imalat hayatimiza 18. yuzyil baslarinda girmistir. 20. yuzyila gelindiginde ise teknolojinin gelismesi ile endustri alaninda vazgecilemez bir noktaya geldi. Bir malzemeye istenilen ozellikleri kazandirmak adina is parcasi ustunden tabaka seklinde malzeme kaldirma islemine denmektedir. Kesici takimlar kullanilarak kalip malzemenin kullanicisinin istenilen sekle girmesi sadece talasli imalat sayesinde olmaktadir.",
        "what_is": "Talasli imalat endustri alaninda cok yaygin kullanilmaktadir. Bu turler belirlenirken yontemleri, tornalama, frezeleme, matkap ile delme veya taslama olarak da farkli turlerde olabilmektedir. Frezleme, kesici takimlar ile birlikte malzemelerden talas kaldirir ve ardindan sekil verilmesidir. Delik delme ise tasarlanmis olan malzemelerin uzerinde silindir bicimde delikler acma islemlerine denir.",
        "methods": "Talasli imalat avantajlari; islenebilen malzeme turunun fazla olmasi, istenilen boyut ve sekilleri kisa surede verilebilir olmasi, istenildigi turde boyutlama yapilabilir olmasi ve temiz yuzeyler saglanmasidir. Nora Paslanmaz ve Celik Firmasi ile talasli imalat yapmaniza yardimci olacak cihaz turlerimiz bulunmaktadir, garanti kosullari ile uygun fiyatlara sunulmaktadir.",
    },
    {
        "slug": "welded-fabrication", "title": "Kaynakli Imalat", "img": "welded_fab",
        "intro": "Imalatin bir cok farkli yerinde kullanilan kaynakli imalat yontemi en cok tercih edilen ve cesitli sektorler icin kritik onemli olan uretim bicimlerindendir. Firmamizda paslanmaz malzemeler, demir, aluminyum ve celik gibi bir cok malzemenin kaynakli imalati kaliteli bir sekilde uretilebilmektedir.",
        "what_is": "Kaynakli imalat sektorunun gunumuzde bu kadar cok tercih edilmesinin sebebi dusuk maliyetler ile hata orani dusuk ve verimliligi yuksek urunler elde edebilmekten kaynaklanmaktadir. Burada onemli olan nokta kaynakli imalatin tercih edilecegi yontemin kullanilacak malzemeye uygun olarak secilmesi gerekliligidir. Firmamiz uzman personelleri projelerinizde sizlere uygun yontemler kullanarak verimli ve maliyeti dusuk uretimler gerceklestirmeniz icin caba sarf etmektedir.",
        "methods": "Uretime baslamadan once tum surecin ince bir sekilde analiz edilmesi, lojistikten baslayarak her etabin planlanmasi uretimin verimliligini saglayacak konularin basinda gelmektedir. Firmamiz her turlu kaynakli imalat islerini kendi makinelerinde isleyerek, basit gorunen imalat cesitlerinden binalara, koprulere, celik yapilardan boru hatlarina kadar pek cok yerde kullanilan kaynakli imalat modelleri tasarlayabilmektedir.",
    },
    {
        "slug": "plasma-cutting", "title": "Plazma Kesim", "img": "plasma",
        "intro": "Plazma kesim, paslanmaz celik sektorunde kullanilan bir kesim yontemidir. Dar bir agiz uctan cikan yuksek hizli iyonize gaz elektrik akimini kesme basligi araciligi ile malzemeye iletir, malzemenin isitilmasini ve boylelikle erimesini saglamaya yaramaktadir.",
        "what_is": "Paslanmaz celik sektorunde sorunsuz ve hatasiz bir kesim yontemi olarak kullanilan bu yontemde ozellikle hasir seklinde metallerin oksi-asetilen kesilmesi mumkun olmayan bazi ozel uygulamalarda plazma kesim yontemleri ile daha iyi sonuclar elde edilmesini saglamaktadir. Plazma kesim yontemini en iyi sekilde kullanan firmamiz bu yontem ile 25 mm altinda celik ve demir disi malzemelerin kesilmesinde konunun uzmanlari tarafindan tavsiye edilmektedir.",
        "methods": "Plazma kesimlerin saglamis oldugu pek cok avantaj bulunmaktadir. Tum iletken metaller uzerinden uygulanabilir olmasi, ayni plaka sac uzerinde birbirinden farkli parcalarin islenip fire oranlarinin en aza indirilmesi, ve neredeyse capaksiz bir kesim saglanmasidir. Nora Paslanmaz ve Celik ile elde ettiginiz plazma kesimlerde yuzey uzerine istenilen amblem, resim vs. resimlendirmeler de yapilabilmektedir.",
    },
    {
        "slug": "laser-cutting", "title": "Lazer Kesim", "img": "laser",
        "intro": "Lazer kesim, malzemeleri kesmek icin bir lazer kullanilarak yapilan islemlere denmektedir. Bu kesim turunde genel olarak endustriyel imalat sektorleri icin kullanilmaktadir. Daha temiz ve puruzsuz kesim yapabilen bir teknoloji olarak bilinmektedir.",
        "what_is": "Lazer kesim kullanilarak yapilan malzeme kesimleri, uretim hatalarini diger cihazlara oranla azaltmaktadir. Bu kesim icerisinde cesitli tezgahlar da uygulanmasi ile kesim islemleri 24 saat gibi kisa surede yapilmaktadir. Seri uretim yapilmasi halinde maliyetlerde cok buyuk olcude azaltilmaktadir.",
        "methods": "Bu cihazlarin birbirinden farkli avantajlari da bulunmaktadir. Etkili zaman yonetimi, kalite, dusuk maliyet, tasarruf, tek seferde en iyi sonucu alma gibi bircok avantaj soylenebilir. Nora Paslanmaz ve Celik ile birlikte sizler de her zaman etkili cozumler alabileceginiz lazer kesim cihazlarini kullanabilirsiniz.",
    },
]

services_body_tr = f"""
<section class="banner" style="background-image:url('{IMG_B64['plasma']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Hizmetler</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">Yetkinliklerimiz</span>
    <h2 class="section-title">Alti hizmet, tek tesis, tedarik, kesim, bukum, kaynak ve talasli imalat bir arada.</h2>
    <p style="font-family:'Poppins'; font-size:15px; color:var(--gray); max-width:640px; line-height:1.8; margin-top:18px; margin-bottom:56px;">Nora paslanmaz ve celik firmasi olarak kuruldugumuz gunden bu yana urun cesitliligi, urunlerindeki saglamlik, kalite ve hizmet kapasitesi ile alanindaki tum firmalar arasinda en iyi hizmetleri sunmaktadir. Ozel uretim alanimizda hizmet veren firmamiz, genis uretim hacmi ve sektor icerisine getirdigi yenilikler sayesinde dikkat cekmekte ve en cok hizmet veren firmalar arasinda oncu bir konuma gelmistir. Gelisen teknoloji ile alt yapisini guclendiren firmamizda demir celik urun satisi, tedarik ve diger konularda hizmetler sunmaktayiz.</p>
  </div>
  <div class="service-grid reveal-stagger">
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['bars']}')"></div>
      <div class="body">
        <span class="idx">01</span>
        <h3><a href="iron-steel-supply.html" style="color:inherit;">Demir Celik Urun</a></h3>
        <p>Sac, profil, boru, hadde urunleri ve celik hasir dogrudan tedarik, talep uzerine kesim ve bukum hizmetiyle birlikte.</p>
        <a class="more" href="iron-steel-supply.html">Devamini Oku</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['cutbend']}')"></div>
      <div class="body">
        <span class="idx">02</span>
        <h3><a href="cutting-bending.html" style="color:inherit;">Kesim Bukum</a></h3>
        <p>CNC pres bukum ile farkli kalinlik ve tonajlarda profil, kosebent ve sekillendirilmis sac.</p>
        <a class="more" href="cutting-bending.html">Devamini Oku</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['cnc']}')"></div>
      <div class="body">
        <span class="idx">03</span>
        <h3><a href="cnc-machining.html" style="color:inherit;">Talasli Imalat</a></h3>
        <p>CNC tornalama, frezeleme, delme ve taslama ile parcalari tam olcusune ve yuzey kalitesine getiriyoruz.</p>
        <a class="more" href="cnc-machining.html">Devamini Oku</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['welded_fab']}')"></div>
      <div class="body">
        <span class="idx">04</span>
        <h3><a href="welded-fabrication.html" style="color:inherit;">Kaynakli Imalat</a></h3>
        <p>Paslanmaz, demir, aluminyum ve celik uzerinde yapisal ve ozel kaynak, tekil parcadan tam montaja kadar.</p>
        <a class="more" href="welded-fabrication.html">Devamini Oku</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['plasma']}')"></div>
      <div class="body">
        <span class="idx">05</span>
        <h3><a href="plasma-cutting.html" style="color:inherit;">Plazma Kesim</a></h3>
        <p>25 mm'ye kadar celik ve demir disi malzemelerde hizli, dusuk fireli iyonize gaz kesimi.</p>
        <a class="more" href="plasma-cutting.html">Devamini Oku</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['laser']}')"></div>
      <div class="body">
        <span class="idx">06</span>
        <h3><a href="laser-cutting.html" style="color:inherit;">Lazer Kesim</a></h3>
        <p>Paslanmaz, demir, aluminyum ve diger saclarda temiz, yuksek hassasiyetli lazer kesim.</p>
        <a class="more" href="laser-cutting.html">Devamini Oku</a>
      </div>
    </div>
  </div>
</section>
"""
write_tr("services", "Hizmetler", "services", services_body_tr)

for svc in service_details_tr:
    body = service_detail_body(svc, service_details_tr, lang="tr")
    write_tr(svc["slug"], svc["title"], "services", body, svc=svc)

# ---------------- TR: PRODUCTS ----------------
demir_body_tr = product_gallery_body("Demir Celik Urunler", "Kategoriye gore demir ve celik urunlerimiz.", demir_items, "profile", lang="tr")
write_tr("demir-celik-urunler", "Demir Celik Urunler", "demir", demir_body_tr)

paslanmaz_body_tr = product_gallery_body("Paslanmaz Urunler", "Kategoriye gore paslanmaz celik urunlerimiz.", paslanmaz_items, "sheet", lang="tr")
write_tr("paslanmaz-urunler", "Paslanmaz Urunler", "paslanmaz", paslanmaz_body_tr)

for key, en_name, native in demir_items + paslanmaz_items:
    is_demir = (key, en_name, native) in demir_items
    cat_href = "demir-celik-urunler.html" if is_demir else "paslanmaz-urunler.html"
    cat_label = NAV_LABELS["tr"]["demir"] if is_demir else NAV_LABELS["tr"]["paslanmaz"]
    body = product_detail_body(key, native, en_name, cat_label, cat_href, "profile" if is_demir else "sheet", lang="tr")
    desc = PRODUCT_INFO[key]["tr"]["what_is"][:160]
    write_tr(product_slug(key), native, "demir" if is_demir else "paslanmaz", body, description=desc)

# ---------------- TR: ABOUT ----------------
about_body_tr = f"""
<section class="banner" style="background-image:url('{BANNER_IMAGES['about_building']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Hakkimizda</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap about-grid reveal">
    <div>
      <span class="section-eyebrow">Biz Kimiz</span>
      <h2 class="section-title" style="margin-bottom:20px;">Paslanmaz ve celik icin uretim ortaginiz.</h2>
      <p>Demir, celik ve paslanmaz celik sektorundeki yillarin deneyimiyle Nora Paslanmaz ve Celik, uzmanlik, hizmet kalitesi ve rekabetci fiyatli urunler ile musterilerine hizmet vermektedir. Nora, sektorunde oncu firmalar arasinda hak ettigi yeri almistir.</p>
      <p>Musteri odakli felsefemizle, surekli arastirma, gelistirme ve kuresel kalite standartlarina bagliligimizla kalite taahhudumuzu surduruyor, sektorde saygin bir isim olarak konumumuzu pekistiriyoruz.</p>
      <p>Nora Paslanmaz ve Celik, deneyimli ve yetkin ekibiyle faaliyetlerinin her asamasini yurutmekte, degerli musterilerimizin satis oncesi ve sonrasinda hicbir zaman deskteksiz kalmamasi icin tam kapasite calismaktadir.</p>
      <div class="about-stats">
        <div class="stat"><b>6</b><span>Temel Surec</span></div>
        <div class="stat"><b>TR</b><span>Istanbul Merkezli</span></div>
        <div class="stat"><b>B2B</b><span>Dogrudan Tedarik</span></div>
      </div>
      <a class="more about-download" href="nora-company-profile.pdf" download="Nora-Sirket-Profili.pdf">Sirket Profilini Indir</a>
    </div>
    <div class="about-visual" style="background-image:url('{IMG_B64['welded_fab']}'); background-size:cover; background-position:center;"></div>
  </div>
</section>
"""
write_tr("about", "Hakkimizda", "about", about_body_tr)

# ---------------- TR: CERTIFICATES ----------------
certificates_body_tr = f"""
<section class="banner" style="background-image:url('{IMG_B64['cnc']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Sertifikalar</h2></div></section>
<section class="partners" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">Sertifikalar ve Referanslar</span>
    <h2 class="section-title" style="margin-bottom:40px;">Sektor paydaslari tarafindan guvenilir.</h2>
  </div>
  <div class="wrap">
  <div class="cert-grid reveal-stagger">
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso9001']}" alt="ISO 9001:2015"><p>ISO 9001:2015<br>Kalite Yonetimi</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso10002']}" alt="ISO 10002:2018"><p>ISO 10002:2018<br>Musteri Memnuniyeti</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso14001']}" alt="ISO 14001:2015"><p>ISO 14001:2015<br>Cevre Yonetimi</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso45001']}" alt="ISO 45001:2018"><p>ISO 45001:2018<br>Is Sagligi ve Guvenligi</p></div>
  </div>
  </div>
</section>
"""
write_tr("certificates", "Sertifikalar", "certificates", certificates_body_tr)

# ---------------- TR: BLOG ----------------
blog_posts_tr = [
    {
        "slug": "iron-steel-products-explained", "title": "Demir Celik Urunleri", "img": "profile",
        "category": "Urunler",
        "excerpt": "Celik, tipik olarak yuzde 0,2 ile yuzde 2,1 arasinda degisen demir ve karbon iceriginin bir kombinasyonundan olusan bir alasimdir.",
        "paragraphs": [
            ("", "Celik, tipik olarak yuzde 0,2 ile yuzde 2,1 arasinda degisen demir ve karbon iceriginin bir kombinasyonundan olusan bir alasimdir. Celik alasimindaki karbon icerigi, celigin siniflandirilmasinda olumlu bir rol oynar. Yuksek firinlarda uretilen demir, gerekli karbonun belirli islemlerden gecerek veya elektrik ark ocaklarinda hurdanin yeniden eritilmesiyle celige donusturulur. Karbon, demiri sertlestiren elementtir ve elde edilen karisimdaki karbon orani ne kadar yuksek olursa celik o kadar sert olur. Nora Paslanmaz ve Celik firmamizda en kaliteli demir celik urunlerini sizlere sunuyoruz."),
            ("Demir Celik Urunleri Nelerdir?", "Demir celik urunleri oldukca cesitlilik gostermektedir. Bu urunler su sekildedir; Npu Profiller, Kosebant, Siyah Sac, Transmisyon, DKP Sac, K Profil, Insaat Demiri, Boyali K Profil, Silme-Lama, Npi Profiller, Kare, Izli Demir, Baklavali Sac, Galvaniz Sac, Galvaniz Trapez Sac, Galvanizli Kare Profiller, Genisletilmis Sac, Su Borusu Galvaniz ve Su Borusu Siyah urunleri icin firmamiz ile iletisime gecmeniz yeterlidir. Alaninda uzman calisanlarimiz ve son model makinelerimiz ile demir celik urunlerinde farkimizi ortaya koymaktayiz."),
            ("Saclar", "Sanayi sektorunde farkli noktalarda kullanilan sac cesitleri bir isletmenin en temel ihtiyacidir. Bir sac imalat firmasindan alabileceginiz saclarin size ozel bir sac kesme tesisi saglamasi gerekir. Bu noktada sizler de sac kesim ihtiyaclarinizi profesyonelce karsilayabilen firmamizi tercih edebilirsiniz. Seri uretimi destekleyebilen levhalar ayni zamanda is maliyetlerinizi de azaltabilir. Sac uretimi firmamiz sac ebatlari ve sac fiyatlari sectiginiz urun ozelliklerine gore degisiklik gosterebilir. Miktarlar yuksek olmadigi surece kalip gerektirmeyen bir islemle sac elde edilebilir. Bu nedenle kullanilan malzemenin deformasyon derecesi neredeyse sifirdir."),
            ("Profiller", "Farkli metallerin farkli kalinliklari ve kaliteleri oldugu icin makine tipleri farkli sekillerde gelir. Bu sebeple hepsini ayni sekilde kesmek mumkun degildir. Kesilen dallar kesilmeden once temizlenmelidir. Islem, kontur kesimi icin gereken hassas kesimleri elde etmek icin celik uzerinde hicbir kalinti kalmamasini saglar. Firmamiz, profil kesim icin uretim suresini kisaltmak icin gerekli tum islemleri yapmaktadir. Urun size montaja ve islemeye hazir olarak teslim edilir. Oksijen, plazma ve lazer kesiciler profil kesme makineleridir."),
            ("Demir Celik Urunlerinin Kullanim Alanlari Nelerdir?", "Demir celik urunleri bircok alanda tercih edilmektedir. Dekorasyon sektorunde dekoratif urunlerin yapilma asamasinda, Otomotiv sektorunde arac alt yapisi olusturma, insaat alanlarinda, Mobilya sektorunde bacak kol portfoyunde, tekstilde aski, manken ya da dokuma tezgahlarinin uretilme asamasinda, Elektronik sektorunde bilgisayar ya da elektronik ekipman uretimi esnasinda, Gemilerde ve agir sanayide tercih edilen demir celik urunleri icin firmamiz sizlere hizmet vermektedir. Kuruldugu andan itibaren profesyonelligi ve kalitesi ile adindan soz ettiren firmamiz, sizler icin en iyi urunleri uretmektedir."),
        ],
    },
    {
        "slug": "stainless-steel-products-explained", "title": "Paslanmaz Celik Urunler", "img": "sheet",
        "category": "Urunler",
        "excerpt": "Paslanmaz celik, celigin icine belirli oranlarda krom karistirilarak elde edilen alasim urunudur.",
        "paragraphs": [
            ("", "Paslanmaz celik gunumuzde bircok imalatta tercih edilen celigin icine belirli oranlarda krom karistirilarak elde edilen alasim urunudur. Uretimde sagladigi pek cok avantaji nedeni ile paslanmaz celige olan talep her gecen sene artis gostermektedir. Nora Paslanmaz Celik firmamiz olarak uzun yillardir sektorun ihtiyaci olan paslanmaz celik urunlerini bunyemizde barindirarak uretimlerinizi aksatmadan sizlere tedarik saglamaktayiz. Firmamizdan verecediniz siparisler icin firmamiz teknik personellerinden urunlerimiz ile ilgili bilgi alabilir ve teknik destek talep edebilirsiniz."),
            ("Paslanmaz Celigin Avantaj Sagladigi Konular", "<em>[Andi icin not: musterinin gonderdigi ekran goruntulerinde bu bolumde bir kayma var, muhtemelen bir kaydirma/foto atlanmis. Asagidaki paragraf o bosluk icin gecici bir koprulemedir, eksik kismi gonderdiginde degistirilmesi gerekiyor.]</em> Paslanmaz celik, uretimde ozellikle korozyona direnc ve tekrarlanan uretimlerde tutarlilik gibi belirgin avantajlar saglar, kalite kaybetmeden uretim yapilmasina olanak taniyor.<br><br>Paslanmaz celik kendi icerisinde cinsine ve kalitesine gore ayrilabilmektedir. Paslanmaz celikte olusabilen bu farkliliklar nedeni ile urunlerinizi guvenilir firmalardan tedarik etmeniz uretimde yasayacaginiz problemleri en aza indirecektir. Paslanmaz celik kalite standartlarina gore korozyona dayanim kuvvetini arttiran bir uzundur. Paslanmaz celik bu farkliliklar ile birlikte kaynak yapilabilirlik orani, islenebilir orani, isil islem alabilme ve mekanik derecesi de degisim gosterebilmektedir. Ornegin bazi paslanmaz celik grubu iceriginde daha az karbon bulunmasi nedeni ile daha elastik ozellikte olabilmektedir. Bu durum islenmesi asamasinda problem yaratabilmektedir. Firmamiz uretim asamasinda kullanacaginiz yere uygun paslanmaz celik urunler hakkinda size detayli bilgi vererek islem yapmaktadir.<br><br>Paslanmaz celik adindan dolayi hicbir sekilde paslanmayacak bir urun olarak bilinmektedir. Ancak bu dogru uretim modelinde dogru paslanmaz celik alasiminin kullanmasina baglidir. Paslanmaz celik kendi uretim ozelliklerine uygun yerlerde kullanildigi takdirde paslanmaz ozelligini korumaktadir. Tersi durumlarda ise paslanmaz ozelligini yitirmektedir. Tum bu incelikler nedeni ile paslanmaz celigin dogru adreslerden temin edilmesi gerekmektedir. Nora paslanmaz celik firmamiz urunler konusunda bilgili ve egitimli ekipleri ile sizlere kaliteli hizmet saglamaktadir."),
            ("Paslanmaz Celik Fiyatlari", "Paslanmaz celik fiyatlari piyasa kosullarina gore farklilik gosterebilmektedir. Paslanmaz celigi satin alirken fiyat onemli bir kistas olmakla birlikte en onemlisi uretiminize uygun paslanmaz celik cesidini bulmaktadir. Dogru urunu almak bu urunlerle yapilmis imalatlarinin uzun sure bir sey olmadan kullanilmasini saglayacaktir. Bunun icin paslanmaz celik satin alirken malzemenin korozyona dayanma gucune, mekanik dayanim gucune, yapacaginiz uretimin sicaklik degerlerine, malzemenin fiziksel ozelliklerine ve yuzey ozelliklerine dikkat etmeniz gerekmektedir. Firmamiz sizlere tum bu teknik konularda gereken destegi vererek satis yapan bir firmadir."),
            ("Paslanmaz Celigin Saklama Kosullari Nasil Olmalidir?", "Paslanmaz celigin bulundurdugunuz yerin ozellikleri urunun deforme olmamasi icin onemlidir. Paslanmaz celigin bekletildigi yerde toprakla temas halinde olmamasi ve karbon celik talasi ile ayni yerde bulundurulmamasi gerekmektedir. Bu hususlara dikkat edilmedigi takdirde paslanmaz celik ozellikleri zarar gorebilmekte ve urunde paslanma belirtileri gorulebilmektedir."),
        ],
    },
]

for post in blog_posts_tr:
    body = blog_detail_body(post, blog_posts_tr, lang="tr")
    write_tr(post["slug"], post["title"], "blog", body)

blog_cards_tr = "\n".join([f"""
    <div class="blog-card">
      <div class="thumb" style="background-image:url('{IMG_B64[p['img']]}'); background-size:cover; background-position:center;"></div>
      <div class="body">
        <span class="date">{p['category']}</span>
        <h3>{p['title']}</h3>
        <p>{p['excerpt']}</p>
        <a class="more" href="{p['slug']}.html">Devamini Oku</a>
      </div>
    </div>""" for p in blog_posts_tr])

blog_body_tr = f"""
<section class="banner" style="background-image:url('{IMG_B64['bars']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Blog</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">Haberler</span>
    <h2 class="section-title">Nora'dan son gelismeler.</h2>
  </div>
  <div class="wrap">
  <div class="blog-grid reveal-stagger">{blog_cards_tr}
  </div>
  </div>
</section>
"""
write_tr("blog", "Blog", "blog", blog_body_tr)

# ---------------- TR: CONTACT ----------------
contact_body_tr = f"""
<section class="banner" style="background-image:url('{BANNER_IMAGES['contact_gate']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Iletisim</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap contact-grid reveal">
    <div>
      <span class="section-eyebrow">Bize Ulasin</span>
      <h2 class="section-title">Teklif isteyin.</h2>
      <ul class="contact-list">
        <li><b>Telefon</b> 0216 621 55 41</li>
        <li><b>E-posta</b> info@norapaslanmazglobal.com</li>
        <li><b>Adres</b> OSB Des Sanayi Sitesi 115 Sok. No:30, Yukari Dudullu, Umraniye / Istanbul</li>
      </ul>
    </div>
    <div class="form-box">
      <form class="ajax-form" data-success="Tesekkurler, talebiniz gonderildi. En kisa surede size donus yapacagiz." data-error="Bir sorun olustu. Lutfen tekrar deneyin ya da bizi arayin.">
        <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
        <input type="hidden" name="subject" value="Yeni Teklif Talebi - Nora Website">
        <input type="checkbox" name="botcheck" style="display:none">
        <div class="form-row"><label>Ad Soyad</label><input type="text" name="name" placeholder="Adiniz" required></div>
        <div class="form-row"><label>E-posta</label><input type="email" name="email" placeholder="siz@firma.com" required></div>
        <div class="form-row"><label>Firma</label><input type="text" name="company" placeholder="Firma adi"></div>
        <div class="form-row"><label>Mesaj</label><textarea name="message" placeholder="Miktar, olcu ve teknik detaylar..." required></textarea></div>
        <button type="submit" class="submit-btn">Talep Gonder</button>
        <p class="form-status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
<section style="padding:0 60px 90px;">
  <div class="map-frame">
    <iframe
      src="https://www.google.com/maps?q=DES+Sanayi+Sitesi,+Nato+Yolu+Cd,+Yukar%C4%B1+Dudullu,+%C3%9Cmraniye%2F%C4%B0stanbul&output=embed"
      width="100%" height="420" style="border:0;" allowfullscreen="" loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>
"""
write_tr("contact", "Iletisim", "contact", contact_body_tr)

# ================= FRENCH (FR) VERSION =================
FR_OUT_DIR = "/home/claude/nora-site/pages/fr"
os.makedirs(FR_OUT_DIR, exist_ok=True)

def write_fr(slug, title, current, body, extra_script="", svc=None, description=None):
    open(f"{FR_OUT_DIR}/{slug}.html", "w").write(page(title, current, body, extra_script, lang="fr", slug=slug, svc=svc, description=description))

# ---------------- FR: HERO ----------------
HERO_SLIDES_FR = [
    ("Service / 01", "Usinage CNC", "cnc", "services.html"),
    ("Service / 02", "D\u00e9coupe Laser", "laser", "services.html"),
    ("Service / 03", "D\u00e9coupe Plasma", "plasma", "services.html"),
    ("Service / 04", "Fabrication Soud\u00e9e", "welded_fab", "services.html"),
    ("Service / 05", "D\u00e9coupe et Pliage", "cutbend", "services.html"),
    ("Produits", "Tubes, Tuyaux et Acier", "pipes", "demir-celik-urunler.html"),
]
HERO_SCRIPT_FR = hero_script(HERO_SLIDES_FR)

home_body_fr = f"""
<div class="hero-spacer" id="heroSpacer"></div>
<div class="hero-fixed" id="heroFixed">
  <div class="hero-viewport">
    <div class="hero-track" id="heroTrack"></div>
  </div>
  <div class="slide-label" id="slideLabel">
    <div class="slide-eyebrow" id="labelEyebrow">Service / 01</div>
    <h1 id="labelTitle">Usinage CNC</h1>
    <div class="slide-rule"></div>
  </div>
  <div class="scroll-hint" id="scrollHint"><div class="line"></div>D\u00c9FILER</div>
</div>
<section class="home-highlights">
  <div class="wrap">
    <div class="hl-grid reveal">
      <div class="hl-intro">
        <span class="section-eyebrow">\u00c0 Propos de Nora</span>
        <h2 class="section-title" style="margin-bottom:20px;">Votre partenaire de fabrication pour l'inox et l'acier.</h2>
        <p>Fort de plusieurs ann\u00e9es d'exp\u00e9rience dans le secteur du fer, de l'acier et de l'acier inoxydable, Nora Paslanmaz ve Celik sert ses clients gr\u00e2ce \u00e0 son expertise, la qualit\u00e9 de son service et des produits \u00e0 prix comp\u00e9titifs.</p>
        <a class="more hl-download" href="../nora-company-profile.pdf" download="Nora-Profil-Entreprise.pdf">T\u00e9l\u00e9charger le Profil</a>
      </div>
      <div class="hl-certs">
        <span class="section-eyebrow">Certifi\u00e9</span>
        <div class="hl-cert-grid">
          <img src="{CERT_IMAGES['cert_iso9001']}" alt="ISO 9001:2015">
          <img src="{CERT_IMAGES['cert_iso14001']}" alt="ISO 14001:2015">
          <img src="{CERT_IMAGES['cert_iso45001']}" alt="ISO 45001:2018">
          <img src="{CERT_IMAGES['cert_iso10002']}" alt="ISO 10002:2018">
        </div>
        <a class="more" href="certificates.html">Tous les Certificats</a>
      </div>
    </div>
    <div class="hl-cta reveal">
      <h3>Pr\u00eat \u00e0 discuter de votre projet ?</h3>
      <a class="more" href="contact.html">Demander un Devis</a>
    </div>
  </div>
</section>
"""
write_fr("index", "Accueil", "home", home_body_fr, HERO_SCRIPT_FR)

# ---------------- FR: SERVICES ----------------
service_details_fr = [
    {
        "slug": "iron-steel-supply", "title": "Fourniture de Fer et d'Acier", "img": "bars",
        "intro": "Outre nos services de d\u00e9coupe, pliage et fabrication, Nora Paslanmaz ve Celik fournit directement une large gamme de produits en fer et en acier, t\u00f4les, profil\u00e9s, tubes, produits lamin\u00e9s et treillis d'acier compris, fabriqu\u00e9s sur des \u00e9quipements modernes et couverts par notre propre garantie de qualit\u00e9.",
        "what_is": "Notre outil de production est con\u00e7u pour de gros volumes et s'appuie sur une technologie actualis\u00e9e, ce qui nous permet de traiter des commandes sur mesure en compl\u00e9ment de notre stock standard. Au-del\u00e0 de la fourniture de mat\u00e9riaux finis, nous proposons \u00e9galement un traitement associ\u00e9 sur demande, notamment la d\u00e9coupe de profil\u00e9s, la d\u00e9coupe de tubes, la d\u00e9coupe de t\u00f4les, le pliage de t\u00f4les et le refendage de bobines, afin qu'une seule commande couvre \u00e0 la fois la mati\u00e8re premi\u00e8re et sa mise en forme.",
        "methods": "Nous nous approvisionnons et fournissons des mat\u00e9riaux pour une large gamme de produits d\u00e9riv\u00e9s, avec des prix comp\u00e9titifs, une qualit\u00e9 constante, une livraison dans les d\u00e9lais et un service apr\u00e8s-vente fiable, et nous livrons partout en Turquie selon le calendrier dont vous avez besoin. Nora Paslanmaz ve Celik travaille selon une approche centr\u00e9e sur le client, contactez directement notre \u00e9quipe pour conna\u00eetre la disponibilit\u00e9 des stocks, poser vos questions techniques ou demander un devis avant de d\u00e9cider.",
    },
    {
        "slug": "cutting-bending", "title": "D\u00e9coupe et Pliage", "img": "cutbend",
        "intro": "Sur nos presses plieuses CNC, nous plions des t\u00f4les de diff\u00e9rentes \u00e9paisseurs et dimensions avec pr\u00e9cision, r\u00e9pondant aux besoins de mise en forme d'un large \u00e9ventail d'industries. Notre \u00e9quipe exp\u00e9riment\u00e9e associe son expertise des mat\u00e9riaux \u00e0 des \u00e9quipements de pliage CNC de haute technologie pour r\u00e9aliser rapidement et avec pr\u00e9cision m\u00eame les travaux de formage de t\u00f4le les plus complexes.",
        "what_is": "La d\u00e9coupe et le pliage sont un m\u00e9tier construit autour de la mise en forme de t\u00f4les et de mati\u00e8res m\u00e9talliques selon les profils dont un projet a r\u00e9ellement besoin, qu'il s'agisse de plaques plates, de corni\u00e8res ou de profil\u00e9s en U utilis\u00e9s notamment dans l'automobile et le b\u00e2timent. Comme il s'agit de la premi\u00e8re \u00e9tape d'une grande partie de la production en aval, r\u00e9ussir cette \u00e9tape dans les d\u00e9lais et aux dimensions demand\u00e9es est d\u00e9terminant pour tout ce qui suit.",
        "methods": "Nos presses plieuses couvrent une gamme de tonnages et de largeurs de travail, chacune associant un poin\u00e7on, une matrice, des axes hydrauliques et une unit\u00e9 de contr\u00f4le CNC, la pression hydraulique serre la t\u00f4le entre des matrices en V assorties pour former chaque pli selon l'angle programm\u00e9. Le type de mat\u00e9riau, l'\u00e9paisseur et la pression requise sont r\u00e9gl\u00e9s via le syst\u00e8me CNC avant le d\u00e9but du formage, ce qui garantit des plis rapides, pr\u00e9cis et reproductibles. Nora Paslanmaz ve Celik associe d\u00e9coupe et pliage \u00e0 nos services de d\u00e9coupe laser et de soudure pour un flux de production continu, avec une assistance disponible \u00e0 tout moment pour vos questions ou nouvelles commandes.",
    },
    {
        "slug": "cnc-machining", "title": "Usinage CNC", "img": "cnc",
        "intro": "L'usinage CNC regroupe les op\u00e9rations de tournage, fraisage, per\u00e7age et rectification qui enl\u00e8vent de la mati\u00e8re \u00e0 une pi\u00e8ce en fines couches pour lui donner sa forme, sa taille et sa finition de surface finales exactes. Il est central dans la fabrication industrielle depuis le 20e si\u00e8cle et reste indispensable partout o\u00f9 la pr\u00e9cision dimensionnelle compte.",
        "what_is": "En usinage CNC (commande num\u00e9rique par ordinateur), des outils de coupe guid\u00e9s par un programme num\u00e9rique enl\u00e8vent de la mati\u00e8re \u00e0 une pi\u00e8ce, que ce soit par tournage, fraisage ou per\u00e7age, jusqu'\u00e0 ce qu'elle atteigne les dimensions exactes du plan. Compar\u00e9es aux m\u00e9thodes manuelles, les machines CNC r\u00e9alisent ce travail plus rapidement et plus s\u00fbrement, ce qui explique aussi leur large utilisation dans les secteurs de l'ameublement et de la fabrication industrielle.",
        "methods": "L'usinage CNC convient \u00e0 une large gamme de mat\u00e9riaux et de finitions, en respectant des tol\u00e9rances dimensionnelles strictes et en produisant des surfaces propres et finies, les pi\u00e8ces pouvant facilement \u00eatre reprises \u00e0 une autre taille ou forme si besoin. Le seul compromis est une petite perte de mati\u00e8re sous forme de chutes pendant la mise en forme, que le mat\u00e9riau soit du m\u00e9tal, du plastique ou du bois, une part normale et attendue du proc\u00e9d\u00e9. Nora Paslanmaz ve Celik propose une gamme compl\u00e8te d'\u00e9quipements de tournage, fraisage et rectification CNC, couverts par des conditions de garantie et une \u00e9quipe exp\u00e9riment\u00e9e pour vous conseiller sur la machine adapt\u00e9e \u00e0 votre projet.",
    },
    {
        "slug": "welded-fabrication", "title": "Fabrication Soud\u00e9e", "img": "welded_fab",
        "intro": "La fabrication soud\u00e9e assemble des composants individuels, en acier inoxydable, fer, aluminium et autres m\u00e9taux, en un seul ensemble structurellement solide. C'est l'une des m\u00e9thodes de fabrication les plus largement utilis\u00e9es au monde, et elle est essentielle dans un grand nombre d'industries.",
        "what_is": "La fabrication soud\u00e9e est choisie parce qu'elle offre des r\u00e9sultats \u00e0 faible taux d'erreur et \u00e0 haute efficacit\u00e9, \u00e0 un co\u00fbt inf\u00e9rieur \u00e0 de nombreuses m\u00e9thodes d'assemblage alternatives, et les progr\u00e8s de l'automatisation l'ont rendue adaptable \u00e0 presque toutes les industries et combinaisons de mat\u00e9riaux. La bonne m\u00e9thode de soudage doit n\u00e9anmoins \u00eatre adapt\u00e9e au mat\u00e9riau assembl\u00e9, c'est pourquoi notre \u00e9quipe exp\u00e9riment\u00e9e planifie chaque projet autour de la technique et de l'\u00e9quipement les mieux adapt\u00e9s, pour une production efficace et \u00e9conomique.",
        "methods": "Comme la fabrication soud\u00e9e r\u00e9compense une planification rigoureuse, nous analysons chaque projet en d\u00e9tail avant le d\u00e9but des travaux, de la logistique jusqu'\u00e0 l'ordre de soudage, afin de limiter les chutes et de tenir le calendrier de livraison convenu pour l'ensemble fini. Nora Paslanmaz ve Celik g\u00e8re ce processus de bout en bout, des petites pi\u00e8ces sur mesure aux travaux structurels pour b\u00e2timents, ponts et r\u00e9seaux de tuyauterie, avec le soutien d'une \u00e9quipe exp\u00e9riment\u00e9e et d'une assistance technique d\u00e8s que votre projet en a besoin.",
    },
    {
        "slug": "plasma-cutting", "title": "D\u00e9coupe Plasma", "img": "plasma",
        "intro": "La d\u00e9coupe plasma utilise un jet de gaz ionis\u00e9 \u00e0 grande vitesse, d\u00e9livr\u00e9 par une buse \u00e9troite, pour chauffer et d\u00e9couper les m\u00e9taux conducteurs d'\u00e9lectricit\u00e9. C'est l'une des m\u00e9thodes les plus rapides pour d\u00e9couper l'acier et d'autres mat\u00e9riaux de structure, et elle est particuli\u00e8rement performante sur les aciers non alli\u00e9s et les t\u00f4les plus \u00e9paisses.",
        "what_is": "En d\u00e9coupe plasma, un gaz ionis\u00e9 est propuls\u00e9 \u00e0 grande vitesse et haute temp\u00e9rature \u00e0 travers une buse \u00e9troite, transportant un courant \u00e9lectrique qui chauffe et fait fondre le m\u00e9tal au contact, tandis que le jet de gaz \u00e0 grande vitesse \u00e9vacue le m\u00e9tal fondu de la d\u00e9coupe. Elle est recommand\u00e9e par les sp\u00e9cialistes du secteur pour d\u00e9couper l'acier et les m\u00e9taux non ferreux jusqu'\u00e0 environ 25 mm d'\u00e9paisseur, y compris pour des cas particuliers, comme les m\u00e9taux en forme de treillis, que la d\u00e9coupe oxyac\u00e9tyl\u00e9nique ne traite pas bien.",
        "methods": "Compar\u00e9e aux m\u00e9thodes de d\u00e9coupe purement m\u00e9caniques, la d\u00e9coupe plasma offre des r\u00e9sultats nettement plus rapides et g\u00e8re facilement les d\u00e9coupes non planes ou irr\u00e9guli\u00e8res. Elle fonctionne sur tout m\u00e9tal conducteur d'\u00e9lectricit\u00e9, et sa technologie permet \u00e9galement un rainurage pr\u00e9cis dans la m\u00eame passe de d\u00e9coupe. En imbriquant plusieurs pi\u00e8ces sur la m\u00eame t\u00f4le, les chutes sont r\u00e9duites au minimum, et le proc\u00e9d\u00e9 lui-m\u00eame produit un bord quasiment sans bavure, avec une d\u00e9formation thermique minimale, m\u00eame \u00e0 travers une mati\u00e8re d'environ 1,5 fois l'\u00e9paisseur de la t\u00f4le. Nora Paslanmaz ve Celik utilise la d\u00e9coupe plasma pour des r\u00e9sultats rapides et pr\u00e9cis \u00e0 des prix comp\u00e9titifs, y compris la gravure d'embl\u00e8mes ou de motifs sur demande.",
    },
    {
        "slug": "laser-cutting", "title": "D\u00e9coupe Laser", "img": "laser",
        "intro": "La d\u00e9coupe laser utilise un faisceau lumineux de forte puissance, pr\u00e9cis\u00e9ment focalis\u00e9, pour d\u00e9couper la t\u00f4le, produisant des bords nets et lisses avec tr\u00e8s peu de reprise. C'est l'une des m\u00e9thodes de d\u00e9coupe les plus utilis\u00e9es dans la fabrication industrielle, appr\u00e9ci\u00e9e pour la qualit\u00e9 de coupe qu'elle produit.",
        "what_is": "En d\u00e9coupe laser, un faisceau lumineux de forte puissance, focalis\u00e9, est guid\u00e9 par un syst\u00e8me automatis\u00e9 sur de l'acier inoxydable, du fer, de l'aluminium et d'autres t\u00f4les m\u00e9talliques, les d\u00e9coupant selon la forme requise. M\u00eame des g\u00e9om\u00e9tries complexes qui prendraient normalement des jours peuvent \u00eatre r\u00e9alis\u00e9es en aussi peu que 24 heures, car le faisceau suit le trac\u00e9 de d\u00e9coupe directement \u00e0 partir du fichier de conception num\u00e9rique.",
        "methods": "Comme le proc\u00e9d\u00e9 est pilot\u00e9 par ordinateur \u00e0 partir du plan d'origine, la d\u00e9coupe laser r\u00e9duit \u00e0 la fois les chutes de mati\u00e8re et les co\u00fbts d'outillage par rapport \u00e0 la d\u00e9coupe conventionnelle, limitant les gabarits et matrices que les anciennes m\u00e9thodes exigent. Elle reste tr\u00e8s pr\u00e9cise m\u00eame \u00e0 haut rendement, avec une erreur humaine r\u00e9duite au minimum malgr\u00e9 l'intensit\u00e9 du proc\u00e9d\u00e9. Nora Paslanmaz ve Celik utilise la d\u00e9coupe laser sur l'acier inoxydable, le fer, l'aluminium et d'autres t\u00f4les m\u00e9talliques, offrant des r\u00e9sultats pr\u00e9cis et \u00e0 prix comp\u00e9titifs pour chaque travail, d'une pi\u00e8ce sur mesure unique \u00e0 une s\u00e9rie compl\u00e8te de production.",
    },
]

services_body_fr = f"""
<section class="banner" style="background-image:url('{IMG_B64['plasma']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Services</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">Nos Comp\u00e9tences</span>
    <h2 class="section-title">Six m\u00e9tiers, un seul site, fourniture, d\u00e9coupe, pliage, soudure et usinage r\u00e9unis.</h2>
    <p style="font-family:'Poppins'; font-size:15px; color:var(--gray); max-width:640px; line-height:1.8; margin-top:18px; margin-bottom:56px;">Depuis notre cr\u00e9ation, Nora Paslanmaz ve Celik se distingue par la diversit\u00e9 de ses produits, la durabilit\u00e9 et la qualit\u00e9 de sa fabrication, et le niveau de service propos\u00e9, ce qui lui vaut une position de premier plan parmi les entreprises du secteur. Fort d'une grande capacit\u00e9 de production et d'une \u00e9quipe exp\u00e9riment\u00e9e et bien \u00e9quip\u00e9e, nous continuons d'investir dans nos infrastructures pour vous proposer fourniture, production sur mesure et transformation, le tout r\u00e9uni au m\u00eame endroit.</p>
  </div>
  <div class="service-grid reveal-stagger">
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['bars']}')"></div>
      <div class="body">
        <span class="idx">01</span>
        <h3><a href="iron-steel-supply.html" style="color:inherit;">Fourniture de Fer et d'Acier</a></h3>
        <p>T\u00f4le, profil\u00e9, tube, produits lamin\u00e9s et treillis d'acier fournis directement, avec d\u00e9coupe et pliage sur demande.</p>
        <a class="more" href="iron-steel-supply.html">En Savoir Plus</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['cutbend']}')"></div>
      <div class="body">
        <span class="idx">02</span>
        <h3><a href="cutting-bending.html" style="color:inherit;">D\u00e9coupe et Pliage</a></h3>
        <p>Pliage sur presse CNC pour profil\u00e9s, corni\u00e8res et t\u00f4les form\u00e9es, dans diff\u00e9rentes \u00e9paisseurs et tonnages.</p>
        <a class="more" href="cutting-bending.html">En Savoir Plus</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['cnc']}')"></div>
      <div class="body">
        <span class="idx">03</span>
        <h3><a href="cnc-machining.html" style="color:inherit;">Usinage CNC</a></h3>
        <p>Tournage, fraisage, per\u00e7age et rectification CNC pour amener les pi\u00e8ces \u00e0 leurs dimensions et finitions exactes.</p>
        <a class="more" href="cnc-machining.html">En Savoir Plus</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['welded_fab']}')"></div>
      <div class="body">
        <span class="idx">04</span>
        <h3><a href="welded-fabrication.html" style="color:inherit;">Fabrication Soud\u00e9e</a></h3>
        <p>Soudure structurelle et sur mesure sur inox, fer, aluminium et acier, de la pi\u00e8ce unique \u00e0 l'ensemble complet.</p>
        <a class="more" href="welded-fabrication.html">En Savoir Plus</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['plasma']}')"></div>
      <div class="body">
        <span class="idx">05</span>
        <h3><a href="plasma-cutting.html" style="color:inherit;">D\u00e9coupe Plasma</a></h3>
        <p>D\u00e9coupe plasma rapide, \u00e0 faibles chutes, sur acier et m\u00e9taux non ferreux jusqu'\u00e0 25 mm.</p>
        <a class="more" href="plasma-cutting.html">En Savoir Plus</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['laser']}')"></div>
      <div class="body">
        <span class="idx">06</span>
        <h3><a href="laser-cutting.html" style="color:inherit;">D\u00e9coupe Laser</a></h3>
        <p>D\u00e9coupe laser nette et de haute pr\u00e9cision sur inox, fer, aluminium et autres t\u00f4les, formes complexes r\u00e9alis\u00e9es rapidement.</p>
        <a class="more" href="laser-cutting.html">En Savoir Plus</a>
      </div>
    </div>
  </div>
</section>
"""
write_fr("services", "Services", "services", services_body_fr)

for svc in service_details_fr:
    body = service_detail_body(svc, service_details_fr, lang="fr")
    write_fr(svc["slug"], svc["title"], "services", body, svc=svc)

# ---------------- FR: PRODUCTS ----------------
demir_body_fr = product_gallery_body("Produits Fer et Acier", "Nos produits en fer et acier, par cat\u00e9gorie.", demir_items, "profile", lang="fr")
write_fr("demir-celik-urunler", "Produits Fer et Acier", "demir", demir_body_fr)

paslanmaz_body_fr = product_gallery_body("Produits Inox", "Nos produits en acier inoxydable, par cat\u00e9gorie.", paslanmaz_items, "sheet", lang="fr")
write_fr("paslanmaz-urunler", "Produits Inox", "paslanmaz", paslanmaz_body_fr)

for key, en_name, native in demir_items + paslanmaz_items:
    is_demir = (key, en_name, native) in demir_items
    cat_href = "demir-celik-urunler.html" if is_demir else "paslanmaz-urunler.html"
    cat_label = NAV_LABELS["fr"]["demir"] if is_demir else NAV_LABELS["fr"]["paslanmaz"]
    fr_name = FR_PRODUCT_NAMES[key]
    body = product_detail_body(key, fr_name, native, cat_label, cat_href, "profile" if is_demir else "sheet", lang="fr")
    desc = PRODUCT_INFO[key]["fr"]["what_is"][:160]
    write_fr(product_slug(key), fr_name, "demir" if is_demir else "paslanmaz", body, description=desc)

# ---------------- FR: ABOUT ----------------
about_body_fr = f"""
<section class="banner" style="background-image:url('{BANNER_IMAGES['about_building']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">\u00c0 Propos</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap about-grid reveal">
    <div>
      <span class="section-eyebrow">Qui Sommes-Nous</span>
      <h2 class="section-title" style="margin-bottom:20px;">Votre partenaire de fabrication pour l'inox et l'acier.</h2>
      <p>Fort de plusieurs ann\u00e9es d'exp\u00e9rience dans le secteur du fer, de l'acier et de l'acier inoxydable, Nora Paslanmaz ve Celik sert ses clients gr\u00e2ce \u00e0 son expertise, la qualit\u00e9 de son service et des produits \u00e0 prix comp\u00e9titifs. Nora a gagn\u00e9 sa place parmi les entreprises leaders du secteur, une position dont nous sommes fiers.</p>
      <p>Guid\u00e9s par une philosophie centr\u00e9e sur le client, notre entreprise reste fid\u00e8le \u00e0 son engagement qualit\u00e9 gr\u00e2ce \u00e0 une recherche et un d\u00e9veloppement continus et au respect des normes de qualit\u00e9 internationales, s'imposant comme un nom reconnu dans le secteur.</p>
      <p>Nora Paslanmaz ve Celik m\u00e8ne chaque aspect de ses activit\u00e9s avec une \u00e9quipe exp\u00e9riment\u00e9e et comp\u00e9tente, travaillant \u00e0 pleine capacit\u00e9 avant et apr\u00e8s chaque vente pour s'assurer que nos clients ne restent jamais sans accompagnement.</p>
      <div class="about-stats">
        <div class="stat"><b>6</b><span>Processus Cl\u00e9s</span></div>
        <div class="stat"><b>TR</b><span>Bas\u00e9 \u00e0 Istanbul</span></div>
        <div class="stat"><b>B2B</b><span>Fourniture Directe</span></div>
      </div>
      <a class="more about-download" href="../nora-company-profile.pdf" download="Nora-Profil-Entreprise.pdf">T\u00e9l\u00e9charger le Profil</a>
    </div>
    <div class="about-visual" style="background-image:url('{IMG_B64['welded_fab']}'); background-size:cover; background-position:center;"></div>
  </div>
</section>
"""
write_fr("about", "\u00c0 Propos", "about", about_body_fr)

# ---------------- FR: CERTIFICATES ----------------
certificates_body_fr = f"""
<section class="banner" style="background-image:url('{IMG_B64['cnc']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Certificats</h2></div></section>
<section class="partners" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">Certificats et R\u00e9f\u00e9rences</span>
    <h2 class="section-title" style="margin-bottom:40px;">La confiance des acteurs du secteur.</h2>
  </div>
  <div class="wrap">
  <div class="cert-grid reveal-stagger">
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso9001']}" alt="ISO 9001:2015"><p>ISO 9001:2015<br>Management de la Qualit\u00e9</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso10002']}" alt="ISO 10002:2018"><p>ISO 10002:2018<br>Satisfaction Client</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso14001']}" alt="ISO 14001:2015"><p>ISO 14001:2015<br>Management Environnemental</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso45001']}" alt="ISO 45001:2018"><p>ISO 45001:2018<br>Sant\u00e9 et S\u00e9curit\u00e9 au Travail</p></div>
  </div>
  </div>
</section>
"""
write_fr("certificates", "Certificats", "certificates", certificates_body_fr)

# ---------------- FR: BLOG ----------------
blog_posts_fr = [
    {
        "slug": "iron-steel-products-explained", "title": "Produits en Fer et Acier", "img": "profile",
        "category": "Produits",
        "excerpt": "L'acier est un alliage de fer et de carbone, et ce dosage d\u00e9termine tout, du classement \u00e0 la duret\u00e9. Un aper\u00e7u de notre gamme et de ses usages.",
        "paragraphs": [
            ("", "L'acier est un alliage compos\u00e9 de fer et de carbone, avec une teneur en carbone comprise g\u00e9n\u00e9ralement entre 0,2 % et 2,1 %. Cette teneur en carbone joue un r\u00f4le cl\u00e9 dans le classement de l'acier. Le fer produit en haut fourneau est converti en acier soit par une s\u00e9rie de proc\u00e9d\u00e9s d'affinage, soit par refonte de ferraille dans des fours \u00e0 arc \u00e9lectrique. Le carbone est l'\u00e9l\u00e9ment qui durcit le fer, plus la proportion de carbone dans le m\u00e9lange obtenu est \u00e9lev\u00e9e, plus l'acier est dur. Chez Nora Paslanmaz ve Celik, nous fournissons \u00e0 nos clients des produits en fer et acier de la plus haute qualit\u00e9."),
            ("Que Sont les Produits en Fer et Acier ?", "Les produits en fer et acier se d\u00e9clinent sous de nombreuses formes. Parmi ce que nous fournissons figurent les profil\u00e9s NPU, les corni\u00e8res, la t\u00f4le noire, les arbres de transmission, la t\u00f4le lamin\u00e9e \u00e0 froid (DKP), les profil\u00e9s en K, les fers \u00e0 b\u00e9ton, les profil\u00e9s en K rev\u00eatus, les fers plats, les profil\u00e9s NPI, les fers carr\u00e9s, les fers nervur\u00e9s, la t\u00f4le stri\u00e9e, la t\u00f4le galvanis\u00e9e, la t\u00f4le trap\u00e9zo\u00efdale galvanis\u00e9e, le profil\u00e9 carr\u00e9 galvanis\u00e9, la t\u00f4le d\u00e9ploy\u00e9e, et les tuyaux d'eau galvanis\u00e9s ou noirs, il vous suffit de contacter notre \u00e9quipe pour l'un de ces produits. Notre personnel sp\u00e9cialis\u00e9 et nos machines modernes font notre diff\u00e9rence en mati\u00e8re de produits en fer et acier."),
            ("T\u00f4le", "La t\u00f4le est l'un des besoins les plus fondamentaux dans la fabrication industrielle, utilis\u00e9e sous diff\u00e9rentes formes selon les applications. Un fournisseur de t\u00f4le doit pouvoir proposer une d\u00e9coupe adapt\u00e9e \u00e0 vos sp\u00e9cifications, c'est exactement ce que nous offrons. La t\u00f4le pr\u00e9sente aussi plusieurs avantages pratiques, un mat\u00e9riau qui permet la production en s\u00e9rie peut r\u00e9duire vos co\u00fbts de production globaux. Les dimensions et le prix de la t\u00f4le varient selon la sp\u00e9cification choisie, le prix \u00e9tant fix\u00e9 en fonction des propri\u00e9t\u00e9s techniques du produit. En dessous d'un certain volume, la t\u00f4le peut \u00eatre produite sans n\u00e9cessiter de matrice du tout, ce qui limite la d\u00e9formation du mat\u00e9riau \u00e0 presque z\u00e9ro."),
            ("Profil\u00e9s", "Comme les diff\u00e9rents m\u00e9taux se d\u00e9clinent en diff\u00e9rentes \u00e9paisseurs et qualit\u00e9s, les machines utilis\u00e9es pour les d\u00e9couper varient en cons\u00e9quence, aucune m\u00e9thode unique ne convient \u00e0 tous les mat\u00e9riaux. Les sections d\u00e9coup\u00e9es sont nettoy\u00e9es avant tout traitement ult\u00e9rieur, une \u00e9tape qui garantit l'absence de r\u00e9sidu sur l'acier, essentielle pour obtenir les d\u00e9coupes de contour pr\u00e9cises que le travail exige. Nous r\u00e9alisons toutes les \u00e9tapes n\u00e9cessaires pour maintenir des d\u00e9lais courts de d\u00e9coupe de profil\u00e9s, et livrons le produit fini pr\u00eat pour l'assemblage ou l'usinage. Les d\u00e9coupeurs \u00e0 oxyg\u00e8ne, plasma et laser sont les machines que nous utilisons pour la d\u00e9coupe de profil\u00e9s."),
            ("O\u00f9 Utilise-t-on les Produits en Fer et Acier ?", "Les produits en fer et acier sont utilis\u00e9s dans un large \u00e9ventail d'industries, en d\u00e9coration, pour des \u00e9l\u00e9ments d\u00e9coratifs, dans l'automobile, pour les structures de soubassement de v\u00e9hicules, dans le b\u00e2timent, dans l'ameublement, pour les pieds et accoudoirs, dans le textile, pour les cintres, mannequins et m\u00e9tiers \u00e0 tisser, en \u00e9lectronique, pour les bo\u00eetiers d'ordinateurs et d'\u00e9quipements, ainsi que dans la construction navale et l'industrie lourde. Nous fournissons des produits en fer et acier pour l'ensemble de ces applications. Depuis sa cr\u00e9ation, notre entreprise s'est forg\u00e9 une r\u00e9putation de professionnalisme et de qualit\u00e9, et nous continuons \u00e0 produire les meilleurs produits possibles pour nos clients."),
        ],
    },
    {
        "slug": "stainless-steel-products-explained", "title": "Produits en Acier Inoxydable", "img": "sheet",
        "category": "Produits",
        "excerpt": "L'acier inoxydable est obtenu en ajoutant du chrome \u00e0 l'acier dans une proportion pr\u00e9cise. Un aper\u00e7u de ses avantages, de sa tarification et de son stockage.",
        "paragraphs": [
            ("", "L'acier inoxydable est un alliage obtenu en ajoutant une proportion pr\u00e9cise de chrome \u00e0 l'acier, et c'est l'un des mat\u00e9riaux les plus utilis\u00e9s dans la fabrication aujourd'hui. En raison des nombreux avantages qu'il offre en production, la demande d'acier inoxydable ne cesse de cro\u00eetre d'ann\u00e9e en ann\u00e9e. Chez Nora Paslanmaz Celik, nous maintenons depuis des ann\u00e9es en stock les produits en acier inoxydable dont notre secteur a besoin, pour vous approvisionner sans perturber votre production. Notre \u00e9quipe technique est disponible pour toute information produit ou assistance technique sur chaque commande que vous passez."),
            ("L\u00e0 O\u00f9 l'Acier Inoxydable Offre un Avantage", "<em>[Note pour Andi : comme dans la version turque, cette section correspond au passage manquant dans les captures d'\u00e9cran du client. Le paragraphe ci-dessous est un texte de liaison provisoire, \u00e0 remplacer une fois la partie manquante re\u00e7ue.]</em> L'acier inoxydable apporte \u00e0 la production des avantages distincts, notamment sa r\u00e9sistance \u00e0 la corrosion et sa r\u00e9gularit\u00e9 au fil des s\u00e9ries de production, permettant de poursuivre la fabrication sans perte de qualit\u00e9.<br><br>L'acier inoxydable se d\u00e9cline lui-m\u00eame en diff\u00e9rents types et qualit\u00e9s. En raison de ces diff\u00e9rences, s'approvisionner aupr\u00e8s d'un fournisseur fiable r\u00e9duit au minimum les probl\u00e8mes qu'elles peuvent causer en production. Selon les normes de qualit\u00e9, l'acier inoxydable est un produit qui accro\u00eet la r\u00e9sistance \u00e0 la corrosion. Outre ces diff\u00e9rences, la soudabilit\u00e9, l'usinabilit\u00e9, l'aptitude au traitement thermique et les propri\u00e9t\u00e9s m\u00e9caniques peuvent aussi varier. Certaines nuances d'acier inoxydable, par exemple, contiennent moins de carbone et sont de ce fait plus \u00e9lastiques, ce qui peut cr\u00e9er des difficult\u00e9s lors de l'usinage. Nous fournissons des conseils d\u00e9taill\u00e9s sur le produit inox adapt\u00e9 \u00e0 votre usage avant tout d\u00e9but de travail.<br><br>Malgr\u00e9 son nom, l'acier inoxydable n'est pas inoxydable en toutes circonstances, cela d\u00e9pend de l'utilisation du bon alliage inoxydable dans le bon proc\u00e9d\u00e9 de production. L'acier inoxydable conserve ses propri\u00e9t\u00e9s anti-taches lorsqu'il est utilis\u00e9 dans les conditions pour lesquelles il est con\u00e7u, et les perd sinon. Pour toutes ces raisons, la provenance de votre acier inoxydable a de l'importance. Notre \u00e9quipe comp\u00e9tente et bien form\u00e9e chez Nora Paslanmaz Celik est l\u00e0 pour vous offrir un service de qualit\u00e9 sur chaque produit."),
            ("Tarification de l'Acier Inoxydable", "Le prix de l'acier inoxydable peut varier selon les conditions du march\u00e9. Si le prix est un crit\u00e8re important \u00e0 l'achat d'acier inoxydable, l'essentiel est de trouver la nuance adapt\u00e9e \u00e0 votre production. Bien choisir garantit que les pi\u00e8ces fabriqu\u00e9es tiendront dans la dur\u00e9e sans probl\u00e8me. Lors de l'achat d'acier inoxydable, il convient de pr\u00eater attention \u00e0 sa r\u00e9sistance \u00e0 la corrosion, sa r\u00e9sistance m\u00e9canique, aux temp\u00e9ratures impliqu\u00e9es dans votre proc\u00e9d\u00e9 de production, ainsi qu'\u00e0 ses propri\u00e9t\u00e9s physiques et de surface. Nous fournissons le soutien technique n\u00e9cessaire sur tous ces points dans le cadre de chaque vente."),
            ("Comment Stocker l'Acier Inoxydable ?", "Le lieu de stockage de l'acier inoxydable d\u00e9termine si le produit reste exempt de d\u00e9formation. Les zones de stockage doivent l'\u00e9loigner de tout contact direct avec le sol, et des copeaux d'acier au carbone stock\u00e9s dans le m\u00eame espace. Si ces pr\u00e9cautions ne sont pas respect\u00e9es, les propri\u00e9t\u00e9s de l'acier inoxydable peuvent \u00eatre compromises et des signes de rouille peuvent appara\u00eetre sur le produit."),
        ],
    },
]

for post in blog_posts_fr:
    body = blog_detail_body(post, blog_posts_fr, lang="fr")
    write_fr(post["slug"], post["title"], "blog", body)

blog_cards_fr = "\n".join([f"""
    <div class="blog-card">
      <div class="thumb" style="background-image:url('{IMG_B64[p['img']]}'); background-size:cover; background-position:center;"></div>
      <div class="body">
        <span class="date">{p['category']}</span>
        <h3>{p['title']}</h3>
        <p>{p['excerpt']}</p>
        <a class="more" href="{p['slug']}.html">En Savoir Plus</a>
      </div>
    </div>""" for p in blog_posts_fr])

blog_body_fr = f"""
<section class="banner" style="background-image:url('{IMG_B64['bars']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Blog</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">Actualit\u00e9s</span>
    <h2 class="section-title">Les derni\u00e8res nouvelles de Nora.</h2>
  </div>
  <div class="wrap">
  <div class="blog-grid reveal-stagger">{blog_cards_fr}
  </div>
  </div>
</section>
"""
write_fr("blog", "Blog", "blog", blog_body_fr)

# ---------------- FR: CONTACT ----------------
contact_body_fr = f"""
<section class="banner" style="background-image:url('{BANNER_IMAGES['contact_gate']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">Contact</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap contact-grid reveal">
    <div>
      <span class="section-eyebrow">Contactez-Nous</span>
      <h2 class="section-title">Demandez un devis.</h2>
      <ul class="contact-list">
        <li><b>T\u00e9l\u00e9phone</b> 0216 621 55 41</li>
        <li><b>E-mail</b> info@norapaslanmazglobal.com</li>
        <li><b>Adresse</b> OSB Des Sanayi Sitesi 115 Sok. No:30, Yukari Dudullu, Umraniye / Istanbul</li>
      </ul>
    </div>
    <div class="form-box">
      <form class="ajax-form" data-success="Merci, votre demande a bien \u00e9t\u00e9 envoy\u00e9e. Nous vous r\u00e9pondrons rapidement." data-error="Une erreur est survenue. Veuillez r\u00e9essayer ou nous appeler directement.">
        <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
        <input type="hidden" name="subject" value="Nouvelle Demande de Devis - Site Nora">
        <input type="checkbox" name="botcheck" style="display:none">
        <div class="form-row"><label>Nom Complet</label><input type="text" name="name" placeholder="Votre nom" required></div>
        <div class="form-row"><label>E-mail</label><input type="email" name="email" placeholder="vous@entreprise.com" required></div>
        <div class="form-row"><label>Entreprise</label><input type="text" name="company" placeholder="Nom de l'entreprise"></div>
        <div class="form-row"><label>Message</label><textarea name="message" placeholder="Quantit\u00e9, dimensions et sp\u00e9cifications..." required></textarea></div>
        <button type="submit" class="submit-btn">Envoyer la Demande</button>
        <p class="form-status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
<section style="padding:0 60px 90px;">
  <div class="map-frame">
    <iframe
      src="https://www.google.com/maps?q=DES+Sanayi+Sitesi,+Nato+Yolu+Cd,+Yukar%C4%B1+Dudullu,+%C3%9Cmraniye%2F%C4%B0stanbul&output=embed"
      width="100%" height="420" style="border:0;" allowfullscreen="" loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>
"""
write_fr("contact", "Contact", "contact", contact_body_fr)

# ================= ARABIC (AR) VERSION =================
AR_OUT_DIR = "/home/claude/nora-site/pages/ar"
os.makedirs(AR_OUT_DIR, exist_ok=True)

def write_ar(slug, title, current, body, extra_script="", svc=None, description=None):
    open(f"{AR_OUT_DIR}/{slug}.html", "w").write(page(title, current, body, extra_script, lang="ar", slug=slug, svc=svc, description=description))

# ---------------- AR: HERO ----------------
HERO_SLIDES_AR = [
    ("خدمة / 01", "التشغيل الآلي CNC", "cnc", "services.html"),
    ("خدمة / 02", "القص بالليزر", "laser", "services.html"),
    ("خدمة / 03", "القص بالبلازما", "plasma", "services.html"),
    ("خدمة / 04", "التصنيع باللحام", "welded_fab", "services.html"),
    ("خدمة / 05", "القص والثني", "cutbend", "services.html"),
    ("منتجات", "أنابيب وبروفايل وصلب", "pipes", "demir-celik-urunler.html"),
]
HERO_SCRIPT_AR = hero_script(HERO_SLIDES_AR)

home_body_ar = f"""
<div class="hero-spacer" id="heroSpacer"></div>
<div class="hero-fixed" id="heroFixed">
  <div class="hero-viewport">
    <div class="hero-track" id="heroTrack"></div>
  </div>
  <div class="slide-label" id="slideLabel">
    <div class="slide-eyebrow" id="labelEyebrow">خدمة / 01</div>
    <h1 id="labelTitle">التشغيل الآلي CNC</h1>
    <div class="slide-rule"></div>
  </div>
  <div class="scroll-hint" id="scrollHint"><div class="line"></div>مرر للأسفل</div>
</div>
<section class="home-highlights">
  <div class="wrap">
    <div class="hl-grid reveal">
      <div class="hl-intro">
        <span class="section-eyebrow">عن نورا</span>
        <h2 class="section-title" style="margin-bottom:20px;">شريكك في تصنيع الستانلس ستيل والصلب.</h2>
        <p>بفضل سنوات من الخبرة في قطاع الحديد والصلب والستانلس ستيل، تخدم نورا للصلب والستانلس عملاءها من خلال الخبرة وجودة الخدمة والمنتجات ذات الأسعار التنافسية.</p>
        <a class="more hl-download" href="../nora-company-profile.pdf" download="Nora-Company-Profile.pdf">تحميل ملف الشركة</a>
      </div>
      <div class="hl-certs">
        <span class="section-eyebrow">معتمد</span>
        <div class="hl-cert-grid">
          <img src="{CERT_IMAGES['cert_iso9001']}" alt="ISO 9001:2015">
          <img src="{CERT_IMAGES['cert_iso14001']}" alt="ISO 14001:2015">
          <img src="{CERT_IMAGES['cert_iso45001']}" alt="ISO 45001:2018">
          <img src="{CERT_IMAGES['cert_iso10002']}" alt="ISO 10002:2018">
        </div>
        <a class="more" href="certificates.html">جميع الشهادات</a>
      </div>
    </div>
    <div class="hl-cta reveal">
      <h3>هل أنت مستعد لمناقشة مشروعك؟</h3>
      <a class="more" href="contact.html">اطلب عرض سعر</a>
    </div>
  </div>
</section>
"""
write_ar("index", "الرئيسية", "home", home_body_ar, HERO_SCRIPT_AR)

# ---------------- AR: SERVICES ----------------
service_details_ar = [
    {
        "slug": "iron-steel-supply", "title": "توريد الحديد والصلب", "img": "bars",
        "intro": "إلى جانب خدمات القص والثني والتصنيع، توفر نورا للصلب والستانلس مجموعة واسعة من منتجات الحديد والصلب مباشرة، بما في ذلك الصاج والبروفايل والأنابيب ومنتجات الدرفلة وشباك الصلب، مُصنّعة على معدات حديثة ومدعومة بضمان الجودة الخاص بنا.",
        "what_is": "منشأتنا الإنتاجية مصممة لأحجام إنتاج كبيرة ومدعومة بتقنية حديثة، مما يتيح لنا تلبية الطلبات المخصصة إلى جانب المخزون القياسي. إلى جانب توريد المواد الجاهزة، نقدم أيضًا معالجة إضافية عند الطلب، تشمل قص البروفايل وقص الأنابيب وقص الصاج وثني الصاج وتقطيع اللفائف، بحيث يغطي طلب واحد المادة الخام وتشكيلها معًا.",
        "methods": "نقوم بتوريد المواد لمجموعة واسعة من المنتجات النهائية، مدعومين بأسعار تنافسية وجودة ثابتة وتسليم في الموعد ودعم موثوق بعد البيع، ونوصّل إلى أي مكان في تركيا وفق الجدول الذي تحتاجه. تعمل نورا للصلب والستانلس على أساس التركيز على العميل، تواصل مع فريقنا مباشرة للاستفسار عن توفر المخزون أو الأسئلة الفنية أو طلب عرض سعر قبل اتخاذ قرارك.",
    },
    {
        "slug": "cutting-bending", "title": "القص والثني", "img": "cutbend",
        "intro": "على مكابس الثني بتقنية CNC لدينا، نقوم بثني الصاج المعدني بمختلف السماكات والأبعاد بدقة، لتلبية احتياجات التشكيل لمجموعة واسعة من الصناعات. يجمع فريقنا ذو الخبرة بين معرفة المواد ومعدات ثني CNC عالية التقنية لإنجاز حتى أصعب أعمال تشكيل الصاج بسرعة ودقة.",
        "what_is": "القص والثني هو مجال يقوم على تشكيل الصاج والمواد المعدنية إلى القطاعات التي يحتاجها المشروع فعليًا، سواء كانت ألواحًا مسطحة أو زوايا أو قطاعات قناة تُستخدم في صناعات مثل السيارات والبناء. ولأنها الخطوة الأولى في الكثير من الإنتاج اللاحق، فإن إنجاز هذه الخطوة بشكل صحيح، في الوقت المحدد وبالأبعاد المطلوبة، أمر مهم لكل ما يليها.",
        "methods": "تغطي مكابسنا مجموعة من الأوزان وعروض العمل، يجمع كل منها بين قالب علوي وقالب سفلي ومحاور هيدروليكية ووحدة تحكم CNC، حيث يضغط الضغط الهيدروليكي الصاج بين قوالب متطابقة على شكل V لتشكيل كل ثنية وفق الزاوية المبرمجة. يتم ضبط نوع المادة والسماكة والضغط المطلوب عبر نظام CNC قبل بدء التشكيل، مما يضمن ثنيًا سريعًا ودقيقًا وقابلًا للتكرار. تجمع نورا للصلب والستانلس بين القص والثني وخدمات القص بالليزر واللحام لدينا في سير عمل إنتاجي متواصل، مع دعم متاح على مدار الساعة للأسئلة أو الطلبات الجديدة.",
    },
    {
        "slug": "cnc-machining", "title": "التشغيل الآلي CNC", "img": "cnc",
        "intro": "يشمل التشغيل الآلي بتقنية CNC عمليات الخراطة والتفريز والحفر والتجليخ التي تُزيل المادة من القطعة على شكل طبقات رقيقة لإعطائها الشكل والحجم والنهاية السطحية النهائية الدقيقة. كانت هذه التقنية محورية في التصنيع الصناعي منذ القرن العشرين وتبقى ضرورية أينما كانت الدقة البُعدية مهمة.",
        "what_is": "في التشغيل الآلي بتقنية CNC (التحكم الرقمي بالحاسوب)، تقوم أدوات القص الموجهة ببرنامج رقمي بإزالة المادة من القطعة، سواء بالخراطة أو التفريز أو الحفر، حتى تصل إلى الأبعاد الدقيقة للتصميم. مقارنة بالطرق اليدوية، تنجز آلات CNC هذا العمل بشكل أسرع وأكثر أمانًا، وهذا أيضًا سبب استخدامها على نطاق واسع في قطاعي الأثاث والتصنيع الصناعي.",
        "methods": "يناسب التشغيل الآلي بتقنية CNC مجموعة واسعة من المواد والتشطيبات، محافظًا على تفاوتات بُعدية دقيقة ومنتجًا أسطحًا نظيفة ومكتملة، مع إمكانية إعادة تشكيل القطع بسهولة إلى حجم أو شكل مختلف عند الحاجة. المقايضة الوحيدة هي فقدان كمية صغيرة من المادة كنُفايات أثناء التشكيل، سواء كانت المادة معدنًا أو بلاستيكًا أو خشبًا، وهو جزء طبيعي ومتوقع من العملية. تقدم نورا للصلب والستانلس مجموعة كاملة من معدات الخراطة والتفريز والتجليخ بتقنية CNC مدعومة بشروط ضمان وفريق ذو خبرة لتقديم المشورة بشأن الآلة المناسبة لعملك.",
    },
    {
        "slug": "welded-fabrication", "title": "التصنيع باللحام", "img": "welded_fab",
        "intro": "يجمع التصنيع باللحام بين المكونات الفردية، من الستانلس ستيل والحديد والألمنيوم ومعادن أخرى، في تجميع واحد متين إنشائيًا. إنها من أكثر طرق التصنيع اعتمادًا على نطاق واسع في العالم، وهي بالغة الأهمية في مجموعة واسعة من الصناعات.",
        "what_is": "يُختار التصنيع باللحام لأنه يحقق نتائج ذات معدل خطأ منخفض وكفاءة عالية، بتكلفة أقل من العديد من طرق الربط البديلة، وقد جعلته التطورات في الأتمتة قابلًا للتكيف مع كل صناعة ومزيج مواد تقريبًا. ومع ذلك، لا تزال طريقة اللحام الصحيحة بحاجة إلى أن تُطابق المادة التي يتم ربطها، ولهذا يخطط فريقنا ذو الخبرة كل مشروع حول التقنية والمعدات الأنسب له، مما يحافظ على كفاءة الإنتاج وفعاليته من حيث التكلفة.",
        "methods": "بما أن التصنيع باللحام يكافئ التخطيط الدقيق، فإننا نحلل كل مشروع بالتفصيل قبل بدء العمل، من اللوجستيات وحتى تسلسل اللحام، للحفاظ على معدلات هدر منخفضة والالتزام بجدول التسليم المتفق عليه للتجميع النهائي. تدير نورا للصلب والستانلس هذه العملية من البداية إلى النهاية، من الكتائف المخصصة الصغيرة إلى الأعمال الإنشائية للمباني والجسور وأنظمة الأنابيب، مدعومة بفريق ذو خبرة ودعم فني كلما احتاج مشروعك ذلك.",
    },
    {
        "slug": "plasma-cutting", "title": "القص بالبلازما", "img": "plasma",
        "intro": "يستخدم القص بالبلازما نفاثًا عالي السرعة من الغاز المؤيَّن، يُوجَّه عبر فوهة ضيقة، لتسخين وقص المعادن الموصلة للكهرباء. إنها من أسرع الطرق المتاحة لقص الصلب والمواد الإنشائية الأخرى، وتؤدي أداءً جيدًا بشكل خاص على الصلب غير المخلوط والصاج ذي السماكة الأكبر.",
        "what_is": "في القص بالبلازما، يُدفع غاز مؤيَّن بسرعة ودرجة حرارة عاليتين عبر فوهة ضيقة، حاملًا تيارًا كهربائيًا يسخّن ويصهر المعدن عند التلامس، بينما يدفع نفاث الغاز عالي السرعة المعدن المنصهر بعيدًا عن منطقة القص. توصي بها الجهات المتخصصة في المجال لقص الصلب والمعادن غير الحديدية حتى سماكة 25 ملم تقريبًا، بما في ذلك حالات خاصة، مثل المعادن على شكل شباك، لا يستطيع القص بالأوكسي-أسيتيلين التعامل معها جيدًا.",
        "methods": "مقارنة بطرق القص الميكانيكية البحتة، يوفر القص بالبلازما نتائج أسرع بشكل ملحوظ ويتعامل بسهولة مع القصات غير المستوية أو غير المنتظمة. يعمل على أي معدن موصل للكهرباء، وتتيح تقنيته أيضًا حفرًا دقيقًا للأخاديد ضمن نفس مسار القص. من خلال ترتيب عدة قطع على نفس اللوح، يتم تقليل الهدر إلى الحد الأدنى، وتنتج العملية نفسها حافة شبه خالية من الزوائد المعدنية مع تشوه حراري بسيط، حتى عبر مواد بسماكة تبلغ حوالي 1.5 ضعف سماكة الصاج. تستخدم نورا للصلب والستانلس القص بالبلازما لتحقيق نتائج سريعة ودقيقة بأسعار تنافسية، بما في ذلك حفر الشعارات أو الرسومات على السطح عند الطلب.",
    },
    {
        "slug": "laser-cutting", "title": "القص بالليزر", "img": "laser",
        "intro": "يستخدم القص بالليزر شعاع ضوء عالي القوة ومركّز بدقة لقص الصاج المعدني، منتجًا حوافًا نظيفة وناعمة مع أقل قدر من المعالجة اللاحقة. إنها من أكثر طرق القص استخدامًا في التصنيع الصناعي، وتحظى بالتقدير لجودة القص التي تنتجها.",
        "what_is": "في القص بالليزر، يوجّه نظام آلي شعاع ضوء عالي القوة ومركّزًا عبر صاج الستانلس ستيل والحديد والألمنيوم ومعادن أخرى، ليقصها إلى الشكل المطلوب. حتى الأشكال الهندسية المعقدة التي تستغرق عادة أيامًا يمكن إنجازها في أقل من 24 ساعة، لأن الشعاع يتبع مسار القص مباشرة من ملف التصميم الرقمي.",
        "methods": "لأن العملية موجهة بالحاسوب من التصميم الأصلي، يقلل القص بالليزر من هدر المواد وتكاليف الأدوات مقارنة بالقص التقليدي، مما يقلل من القوالب والأدوات التي تتطلبها الطرق القديمة. تبقى دقيقة جدًا حتى مع الإنتاج العالي، مع تقليل الخطأ البشري إلى الحد الأدنى رغم كثافة العملية. تستخدم نورا للصلب والستانلس القص بالليزر على صاج الستانلس ستيل والحديد والألمنيوم ومعادن أخرى، لتقديم نتائج دقيقة وبأسعار تنافسية لكل عمل، من القطعة المخصصة الواحدة إلى دفعة الإنتاج الكاملة.",
    },
]

services_body_ar = f"""
<section class="banner" style="background-image:url('{IMG_B64['plasma']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">الخدمات</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">قدراتنا</span>
    <h2 class="section-title">ست خدمات، منشأة واحدة، التوريد والقص والثني واللحام والتشغيل الآلي مجتمعة.</h2>
    <p style="font-family:'Poppins'; font-size:15px; color:var(--gray); max-width:640px; line-height:1.8; margin-top:18px; margin-bottom:56px;">منذ تأسيسنا، تتميز نورا للصلب والستانلس بتنوع منتجاتها ومتانة وجودة تصنيعها ومستوى الخدمة المقدمة، مما أكسبها مكانة رائدة بين شركات القطاع. بفضل قدرة إنتاجية كبيرة وفريق ذو خبرة ومجهّز جيدًا، نواصل الاستثمار في بنيتنا التحتية لنقدم لكم التوريد والإنتاج المخصص والمعالجة، كل ذلك في مكان واحد.</p>
  </div>
  <div class="service-grid reveal-stagger">
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['bars']}')"></div>
      <div class="body">
        <span class="idx">01</span>
        <h3><a href="iron-steel-supply.html" style="color:inherit;">توريد الحديد والصلب</a></h3>
        <p>صاج وبروفايل وأنابيب ومنتجات درفلة وشباك صلب تُورَّد مباشرة، مع خدمات القص والثني عند الطلب.</p>
        <a class="more" href="iron-steel-supply.html">اعرف المزيد</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['cutbend']}')"></div>
      <div class="body">
        <span class="idx">02</span>
        <h3><a href="cutting-bending.html" style="color:inherit;">القص والثني</a></h3>
        <p>ثني بمكابس CNC لبروفايل وزوايا وصاج مُشكّل، بمختلف السماكات والأوزان.</p>
        <a class="more" href="cutting-bending.html">اعرف المزيد</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['cnc']}')"></div>
      <div class="body">
        <span class="idx">03</span>
        <h3><a href="cnc-machining.html" style="color:inherit;">التشغيل الآلي CNC</a></h3>
        <p>خراطة وتفريز وحفر وتجليخ بتقنية CNC لإحضار القطع إلى أبعادها ونهايتها السطحية الدقيقة.</p>
        <a class="more" href="cnc-machining.html">اعرف المزيد</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['welded_fab']}')"></div>
      <div class="body">
        <span class="idx">04</span>
        <h3><a href="welded-fabrication.html" style="color:inherit;">التصنيع باللحام</a></h3>
        <p>لحام إنشائي ومخصص على الستانلس ستيل والحديد والألمنيوم والصلب، من القطعة الواحدة إلى التجميع الكامل.</p>
        <a class="more" href="welded-fabrication.html">اعرف المزيد</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['plasma']}')"></div>
      <div class="body">
        <span class="idx">05</span>
        <h3><a href="plasma-cutting.html" style="color:inherit;">القص بالبلازما</a></h3>
        <p>قص بالبلازما سريع وبهدر منخفض للصلب والمعادن غير الحديدية حتى 25 ملم.</p>
        <a class="more" href="plasma-cutting.html">اعرف المزيد</a>
      </div>
    </div>
    <div class="service-card">
      <div class="thumb" style="background-image:url('{IMG_B64['laser']}')"></div>
      <div class="body">
        <span class="idx">06</span>
        <h3><a href="laser-cutting.html" style="color:inherit;">القص بالليزر</a></h3>
        <p>قص بالليزر نظيف وعالي الدقة على الستانلس ستيل والحديد والألمنيوم وصاج آخر، أشكال معقدة تُنجز بسرعة.</p>
        <a class="more" href="laser-cutting.html">اعرف المزيد</a>
      </div>
    </div>
  </div>
</section>
"""
write_ar("services", "الخدمات", "services", services_body_ar)

for svc in service_details_ar:
    body = service_detail_body(svc, service_details_ar, lang="ar")
    write_ar(svc["slug"], svc["title"], "services", body, svc=svc)

# ---------------- AR: PRODUCTS ----------------
demir_body_ar = product_gallery_body("منتجات الحديد والصلب", "منتجات الحديد والصلب لدينا، حسب الفئة.", demir_items, "profile", lang="ar")
write_ar("demir-celik-urunler", "منتجات الحديد والصلب", "demir", demir_body_ar)

paslanmaz_body_ar = product_gallery_body("منتجات الستانلس ستيل", "منتجات الستانلس ستيل لدينا، حسب الفئة.", paslanmaz_items, "sheet", lang="ar")
write_ar("paslanmaz-urunler", "منتجات الستانلس ستيل", "paslanmaz", paslanmaz_body_ar)

for key, en_name, native in demir_items + paslanmaz_items:
    is_demir = (key, en_name, native) in demir_items
    cat_href = "demir-celik-urunler.html" if is_demir else "paslanmaz-urunler.html"
    cat_label = NAV_LABELS["ar"]["demir"] if is_demir else NAV_LABELS["ar"]["paslanmaz"]
    ar_name = AR_PRODUCT_NAMES[key]
    body = product_detail_body(key, ar_name, native, cat_label, cat_href, "profile" if is_demir else "sheet", lang="ar")
    desc = PRODUCT_INFO[key]["ar"]["what_is"][:160]
    write_ar(product_slug(key), ar_name, "demir" if is_demir else "paslanmaz", body, description=desc)

# ---------------- AR: ABOUT ----------------
about_body_ar = f"""
<section class="banner" style="background-image:url('{BANNER_IMAGES['about_building']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">من نحن</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap about-grid reveal">
    <div>
      <span class="section-eyebrow">من نحن</span>
      <h2 class="section-title" style="margin-bottom:20px;">شريكك في تصنيع الستانلس ستيل والصلب.</h2>
      <p>بفضل سنوات من الخبرة في قطاع الحديد والصلب والستانلس ستيل، تخدم نورا للصلب والستانلس عملاءها من خلال الخبرة وجودة الخدمة والمنتجات ذات الأسعار التنافسية. اكتسبت نورا مكانتها بين الشركات الرائدة في القطاع، وهي مكانة نفخر بها.</p>
      <p>بفلسفة تركز على العميل، تحافظ شركتنا على التزامها بالجودة من خلال البحث والتطوير المستمرين والالتزام بمعايير الجودة العالمية، مما يرسخ مكانتها كاسم مرموق في القطاع.</p>
      <p>تُدير نورا للصلب والستانلس كل جانب من جوانب عملياتها بفريق ذي خبرة وكفاءة، يعمل بكامل طاقته قبل وبعد كل عملية بيع لضمان ألا يبقى عملاؤنا الكرام دون دعم أبدًا.</p>
      <div class="about-stats">
        <div class="stat"><b>6</b><span>عمليات أساسية</span></div>
        <div class="stat"><b>TR</b><span>مقرها إسطنبول</span></div>
        <div class="stat"><b>B2B</b><span>توريد مباشر</span></div>
      </div>
      <a class="more about-download" href="../nora-company-profile.pdf" download="Nora-Company-Profile.pdf">تحميل ملف الشركة</a>
    </div>
    <div class="about-visual" style="background-image:url('{IMG_B64['welded_fab']}'); background-size:cover; background-position:center;"></div>
  </div>
</section>
"""
write_ar("about", "من نحن", "about", about_body_ar)

# ---------------- AR: CERTIFICATES ----------------
certificates_body_ar = f"""
<section class="banner" style="background-image:url('{IMG_B64['cnc']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">الشهادات</h2></div></section>
<section class="partners" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">الشهادات والمراجع</span>
    <h2 class="section-title" style="margin-bottom:40px;">موثوق بها من قبل شركاء القطاع.</h2>
  </div>
  <div class="wrap">
  <div class="cert-grid reveal-stagger">
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso9001']}" alt="ISO 9001:2015"><p>ISO 9001:2015<br>إدارة الجودة</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso10002']}" alt="ISO 10002:2018"><p>ISO 10002:2018<br>رضا العملاء</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso14001']}" alt="ISO 14001:2015"><p>ISO 14001:2015<br>الإدارة البيئية</p></div>
    <div class="cert-card"><img src="{CERT_IMAGES['cert_iso45001']}" alt="ISO 45001:2018"><p>ISO 45001:2018<br>الصحة والسلامة المهنية</p></div>
  </div>
  </div>
</section>
"""
write_ar("certificates", "الشهادات", "certificates", certificates_body_ar)

# ---------------- AR: BLOG ----------------
blog_posts_ar = [
    {
        "slug": "iron-steel-products-explained", "title": "منتجات الحديد والصلب", "img": "profile",
        "category": "منتجات",
        "excerpt": "الصلب سبيكة من الحديد والكربون، وهذه النسبة تحدد كل شيء من التصنيف إلى الصلابة. نظرة على مجموعتنا واستخداماتها.",
        "paragraphs": [
            ("", "الصلب سبيكة تتكون من مزيج من الحديد والكربون، تتراوح نسبة الكربون فيها عادة بين 0.2% و2.1%. تلعب نسبة الكربون دورًا رئيسيًا في تصنيف الصلب. يتحول الحديد المنتج في الأفران العالية إلى صلب إما من خلال سلسلة من عمليات التكرير أو بإعادة صهر الخردة في أفران القوس الكهربائي. الكربون هو العنصر الذي يصلّب الحديد، وكلما ارتفعت نسبة الكربون في المزيج الناتج، زادت صلابة الصلب. في نورا للصلب والستانلس، نزوّد عملاءنا بأجود منتجات الحديد والصلب."),
            ("ما هي منتجات الحديد والصلب؟", "تأتي منتجات الحديد والصلب بأشكال متعددة. من بين ما نورده بروفايل NPU، الزوايا، الصاج الأسود، أعمدة نقل الحركة، الصاج المدرفل على البارد (DKP)، بروفايل K، حديد التسليح، بروفايل K المطلي، الحديد المسطح، بروفايل NPI، الحديد المربع، الحديد المضلع، الصاج المعشّق، الصاج المجلفن، الصاج المجلفن شبه المنحرف، البروفايل المربع المجلفن، الصاج الموسّع، وأنابيب المياه المجلفنة أو السوداء، يكفي التواصل مع فريقنا لأي من هذه المنتجات. طاقمنا المتخصص وآلاتنا الحديثة هي ما يميزنا في منتجات الحديد والصلب."),
            ("الصاج", "الصاج من أهم الاحتياجات الأساسية في التصنيع الصناعي، يُستخدم بأشكال مختلفة حسب التطبيقات. يجب أن يكون مورّد الصاج قادرًا على تقديم قص مصمم حسب مواصفاتك، وهذا بالضبط ما نقدمه. يقدم الصاج أيضًا عدة مزايا عملية، فالمادة التي تدعم الإنتاج المتسلسل يمكن أن تقلل من تكاليف الإنتاج الإجمالية لديك. تختلف أبعاد الصاج وأسعاره حسب المواصفات التي تختارها، ويُحدَّد السعر وفق الخصائص الفنية للمنتج. دون حجم معين، يمكن إنتاج الصاج دون الحاجة إلى قالب على الإطلاق، مما يبقي تشوه المادة قريبًا من الصفر."),
            ("البروفايل", "بما أن المعادن المختلفة تأتي بسماكات ودرجات مختلفة، تختلف الآلات المستخدمة لقصها تبعًا لذلك، فلا توجد طريقة واحدة تناسب كل المواد. تُنظّف الأقسام المقطوعة قبل أي معالجة إضافية، وهي خطوة تضمن عدم بقاء أي بقايا على الصلب، وهو أمر أساسي لتحقيق قصات المحيط الدقيقة التي يتطلبها العمل. نقوم بجميع الخطوات اللازمة للحفاظ على مدة قصيرة لقص البروفايل، ونسلّم المنتج النهائي جاهزًا للتركيب أو المعالجة الإضافية. تُعد قواطع الأكسجين والبلازما والليزر الآلات التي نستخدمها لقص البروفايل."),
            ("أين تُستخدم منتجات الحديد والصلب؟", "تُختار منتجات الحديد والصلب في مجموعة واسعة من الصناعات، في الديكور، للتجهيزات الزخرفية، في السيارات، لهياكل أسفل المركبات، في البناء، في الأثاث، للأرجل والمساند، في النسيج، للشماعات والمانيكانات وأنوال النسج، في الإلكترونيات، لهياكل أجهزة الحاسوب والمعدات، وفي بناء السفن والصناعات الثقيلة. نزوّد منتجات الحديد والصلب لجميع هذه التطبيقات. منذ يوم تأسيسها، بنت شركتنا اسمًا للاحترافية والجودة، ونواصل إنتاج أفضل المنتجات الممكنة لعملائنا."),
        ],
    },
    {
        "slug": "stainless-steel-products-explained", "title": "منتجات الستانلس ستيل", "img": "sheet",
        "category": "منتجات",
        "excerpt": "يُصنع الستانلس ستيل بإضافة الكروم إلى الصلب بنسبة محددة. نظرة على مزاياه وتسعيره وتخزينه.",
        "paragraphs": [
            ("", "الستانلس ستيل سبيكة تُصنع بإضافة نسبة محددة من الكروم إلى الصلب، وهو من أكثر المواد استخدامًا في التصنيع اليوم. بسبب المزايا العديدة التي يوفرها في الإنتاج، يستمر الطلب على الستانلس ستيل في النمو عامًا بعد عام. في نورا للصلب والستانلس، حافظنا لسنوات على توفر منتجات الستانلس ستيل التي يحتاجها قطاعنا في المخزون، لتزويدكم دون تعطيل إنتاجكم. فريقنا الفني متاح لتقديم معلومات المنتج والدعم الفني على أي طلب تقومون به."),
            ("أين يقدم الستانلس ستيل ميزة؟", "<em>[ملاحظة لأندي: كما في النسخة التركية، هذا القسم يقابل الجزء المفقود في لقطات الشاشة التي أرسلها العميل. الفقرة أدناه نص ربط مؤقت لهذه الفجوة، يجب استبدالها بمجرد استلام الجزء الناقص.]</em> يوفر الستانلس ستيل للإنتاج مزايا مميزة، خاصة مقاومته للتآكل واتساقه عبر دورات الإنتاج المتكررة، مما يتيح استمرار التصنيع دون فقدان الجودة.<br><br>ينقسم الستانلس ستيل نفسه إلى أنواع ودرجات مختلفة. بسبب هذه الاختلافات القائمة في الستانلس ستيل، فإن توريد المواد من مورّد موثوق يقلل إلى الحد الأدنى من المشاكل التي قد تسببها في الإنتاج. وفقًا لمعايير الجودة، الستانلس ستيل منتج يزيد من مقاومة التآكل. إلى جانب هذه الاختلافات، يمكن أن تتفاوت أيضًا قابلية اللحام وقابلية التشغيل والقدرة على المعالجة الحرارية والدرجة الميكانيكية. على سبيل المثال، تحتوي بعض مجموعات الستانلس ستيل على كربون أقل مما يجعلها أكثر مرونة، وهو ما قد يخلق مشاكل أثناء التشغيل. نقدم إرشادات مفصلة حول منتج الستانلس ستيل المناسب لاستخدامكم المقصود قبل بدء أي عمل.<br><br>رغم اسمه، الستانلس ستيل ليس مقاومًا للصدأ في جميع الظروف، وهذا يعتمد على استخدام سبيكة الستانلس ستيل الصحيحة في عملية الإنتاج الصحيحة. يحافظ الستانلس ستيل على خصائصه المقاومة للتلطخ عند استخدامه في الظروف المناسبة له، ويفقدها في غير ذلك. لكل هذه الأسباب، من المهم من أين تحصلون على الستانلس ستيل الخاص بكم. فريقنا المطّلع والمدرّب جيدًا في نورا للصلب والستانلس هنا لتقديم خدمة عالية الجودة لكم على كل منتج."),
            ("أسعار الستانلس ستيل", "يمكن أن تختلف أسعار الستانلس ستيل حسب ظروف السوق. بينما يُعد السعر معيارًا مهمًا عند شراء الستانلس ستيل، فإن الأهم هو إيجاد الدرجة المناسبة لإنتاجكم. اختيار المنتج الصحيح يضمن أن القطع المصنوعة منه ستدوم طويلاً دون مشاكل. لهذا، عند شراء الستانلس ستيل، يجب الانتباه إلى مقاومته للتآكل وقوته الميكانيكية ودرجات الحرارة التي ينطوي عليها إنتاجكم وخصائصه الفيزيائية والسطحية. نقدم لكم الدعم الفني اللازم في جميع هذه النقاط كجزء من كل عملية بيع."),
            ("كيف يجب تخزين الستانلس ستيل؟", "يؤثر مكان تخزين الستانلس ستيل على ما إذا كان المنتج سيبقى خاليًا من التشوه. يجب أن تُبقي مناطق التخزين المنتج بعيدًا عن التلامس المباشر مع التربة، وبعيدًا عن برادة الصلب الكربوني المخزنة في نفس المساحة. إذا لم تُراعَ هذه الاحتياطات، يمكن أن تتأثر خصائص الستانلس ستيل وقد تظهر علامات صدأ على المنتج."),
        ],
    },
]

for post in blog_posts_ar:
    body = blog_detail_body(post, blog_posts_ar, lang="ar")
    write_ar(post["slug"], post["title"], "blog", body)

blog_cards_ar = "\n".join([f"""
    <div class="blog-card">
      <div class="thumb" style="background-image:url('{IMG_B64[p['img']]}'); background-size:cover; background-position:center;"></div>
      <div class="body">
        <span class="date">{p['category']}</span>
        <h3>{p['title']}</h3>
        <p>{p['excerpt']}</p>
        <a class="more" href="{p['slug']}.html">اقرأ المزيد</a>
      </div>
    </div>""" for p in blog_posts_ar])

blog_body_ar = f"""
<section class="banner" style="background-image:url('{IMG_B64['bars']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">المدونة</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap">
    <span class="section-eyebrow">أخبار وتحديثات</span>
    <h2 class="section-title">آخر مستجدات نورا.</h2>
  </div>
  <div class="wrap">
  <div class="blog-grid reveal-stagger">{blog_cards_ar}
  </div>
  </div>
</section>
"""
write_ar("blog", "المدونة", "blog", blog_body_ar)

# ---------------- AR: CONTACT ----------------
contact_body_ar = f"""
<section class="banner" style="background-image:url('{BANNER_IMAGES['contact_gate']}'); background-size:cover; background-position:center;"><div class="banner-content reveal"><h2 class="serif">اتصل بنا</h2></div></section>
<section class="section" style="padding-top:70px;">
  <div class="wrap contact-grid reveal">
    <div>
      <span class="section-eyebrow">تواصل معنا</span>
      <h2 class="section-title">اطلب عرض سعر.</h2>
      <ul class="contact-list">
        <li><b>الهاتف</b> 0216 621 55 41</li>
        <li><b>البريد الإلكتروني</b> info@norapaslanmazglobal.com</li>
        <li><b>العنوان</b> OSB Des Sanayi Sitesi 115 Sok. No:30, Yukari Dudullu, Umraniye / Istanbul</li>
      </ul>
    </div>
    <div class="form-box">
      <form class="ajax-form" data-success="شكرًا لكم، تم إرسال طلبكم. سنعاود التواصل معكم قريبًا." data-error="حدث خطأ ما. يرجى المحاولة مرة أخرى أو الاتصال بنا مباشرة.">
        <input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
        <input type="hidden" name="subject" value="طلب عرض سعر جديد - موقع نورا">
        <input type="checkbox" name="botcheck" style="display:none">
        <div class="form-row"><label>الاسم الكامل</label><input type="text" name="name" placeholder="اسمك" required></div>
        <div class="form-row"><label>البريد الإلكتروني</label><input type="email" name="email" placeholder="you@company.com" required></div>
        <div class="form-row"><label>الشركة</label><input type="text" name="company" placeholder="اسم الشركة"></div>
        <div class="form-row"><label>الرسالة</label><textarea name="message" placeholder="الكمية والأبعاد وأي تفاصيل فنية..." required></textarea></div>
        <button type="submit" class="submit-btn">إرسال الطلب</button>
        <p class="form-status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
<section style="padding:0 60px 90px;">
  <div class="map-frame">
    <iframe
      src="https://www.google.com/maps?q=DES+Sanayi+Sitesi,+Nato+Yolu+Cd,+Yukar%C4%B1+Dudullu,+%C3%9Cmraniye%2F%C4%B0stanbul&output=embed"
      width="100%" height="420" style="border:0;" allowfullscreen="" loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>
"""
write_ar("contact", "اتصل بنا", "contact", contact_body_ar)

print("done")
