// Stars background
(function() {
  const canvas = document.getElementById('stars');
  const ctx = canvas.getContext('2d');
  let stars = [];

  function resize() {
    canvas.width = canvas.offsetWidth * devicePixelRatio;
    canvas.height = canvas.offsetHeight * devicePixelRatio;
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.scale(devicePixelRatio, devicePixelRatio);
    init();
  }

  function init() {
    const w = canvas.offsetWidth, h = canvas.offsetHeight;
    const count = Math.min(Math.floor((w * h) / 3000), 1000);
    stars = [];
    for (let i = 0; i < count; i++) {
      stars.push({
        x: Math.random() * w,
        y: Math.random() * h,
        r: Math.random() * 1.2 + 0.3,
        base: Math.random() * 0.4 + 0.1,
        speed: Math.random() * 0.008 + 0.003,
        offset: Math.random() * Math.PI * 2
      });
    }
  }

  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function draw(t) {
    if (prefersReducedMotion) return;
    ctx.clearRect(0, 0, canvas.offsetWidth, canvas.offsetHeight);
    for (const s of stars) {
      const alpha = s.base + Math.sin(t * s.speed + s.offset) * 0.15;
      ctx.fillStyle = `rgba(255,255,255,${alpha})`;
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fill();
    }
    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize);
  resize();
  requestAnimationFrame(draw);
})();

// Mobile nav toggle
(function() {
  var btn = document.getElementById('hamburger');
  var nav = document.getElementById('mobileNav');
  var closeBtn = document.getElementById('mobileNavClose');
  function openNav() { btn.classList.add('active'); nav.classList.add('open'); }
  function closeNav() { btn.classList.remove('active'); nav.classList.remove('open'); }
  btn.addEventListener('click', function() {
    nav.classList.contains('open') ? closeNav() : openNav();
  });
  closeBtn.addEventListener('click', closeNav);
  nav.querySelectorAll('a').forEach(function(a) {
    a.addEventListener('click', closeNav);
  });
})();

// Email obfuscation — assembled at runtime to defeat scrapers
(function() {
  var b = document.getElementById('contact-btn');
  var disp = document.getElementById('email-display');
  var u = 'hello'; var d = 'kuzln'; var t = 'ai';
  var addr = u + '@' + d + '.' + t;
  b.addEventListener('click', function(e) {
    e.preventDefault();
    window.location.href = 'mail' + 'to:' + addr;
  });
  b.textContent = 'Start a Project';
  if (disp) disp.textContent = addr;
  // Uncomment and set your Calendly URL to enable the booking button:
  // var bookBtn = document.getElementById('book-btn');
  // bookBtn.style.display = 'block';
  // bookBtn.href = 'https://calendly.com/YOUR_LINK';
})();

// Animated favicon — spinning arc with fixed sparks
(function() {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var size = 64;
  var c = document.createElement('canvas');
  c.width = size; c.height = size;
  var ctx = c.getContext('2d');
  var link = document.querySelector('link[rel="icon"]');
  var cx = size / 2, cy = size / 2;
  var radius = size * 0.28;
  var thick = size * 0.0875;
  var baseRotation = 12 * Math.PI / 180;
  var rpm = 1 / 6.25;

  var scale = size / 400;

  var sparks = [
    [321.7,244.3,362.5,263.3],[321.7,244.3,361.0,266.2],[321.7,244.3,359.4,268.9],
    [321.7,244.3,375.4,285.2],[321.7,244.3,396.0,309.7],[321.7,244.3,369.0,292.4],
    [321.7,244.3,350.9,278.5],[321.7,244.3,361.7,298.6],[321.7,244.3,345.7,282.3],
    [321.7,244.3,342.9,284.0],[321.7,244.3,340.1,285.4],[321.7,244.3,337.1,286.6]
  ];

  function drawArc(ctx, spinAngle) {
    var segments = 40;
    var startA = 20 * Math.PI / 180;
    var endA = 366 * Math.PI / 180;
    var r = 112 * scale;
    var maxThick = 35 * scale;
    var endTaper = 3 * Math.PI / 180;

    var outer = [], inner = [];
    for (var i = 0; i <= segments; i++) {
      var t = i / segments;
      var a = startA + t * (endA - startA);
      var deg = a * 180 / Math.PI;
      var tf = deg <= 180 ? 0.45 + (0.55 * (deg - 60) / 120) : 1.0;
      var th = maxThick * tf;
      var oR = r + th / 2;
      var iR = r - th / 2;
      var oA = a, iA = a;
      if (i === segments) { oA = a + endTaper; iA = a - endTaper; }
      outer.push([cx + oR * Math.cos(oA + spinAngle), cy + oR * Math.sin(oA + spinAngle)]);
      inner.push([cx + iR * Math.cos(iA + spinAngle), cy + iR * Math.sin(iA + spinAngle)]);
    }

    ctx.beginPath();
    ctx.moveTo(outer[0][0], outer[0][1]);
    for (var i = 1; i <= segments; i++) ctx.lineTo(outer[i][0], outer[i][1]);
    ctx.lineTo(inner[segments][0], inner[segments][1]);
    for (var i = segments; i >= 0; i--) ctx.lineTo(inner[i][0], inner[i][1]);
    ctx.closePath();

    var grd = ctx.createLinearGradient(0, 0, size, size);
    grd.addColorStop(0, '#FFF0E0');
    grd.addColorStop(0.5, '#E8642C');
    grd.addColorStop(1, '#C0401A');
    ctx.fillStyle = grd;
    ctx.fill();
  }

  var lastFaviconFrame = 0;
  var faviconInterval = 100;

  function drawFavicon(t) {
    if (prefersReducedMotion) return;
    if (t - lastFaviconFrame < faviconInterval) {
      requestAnimationFrame(drawFavicon);
      return;
    }
    lastFaviconFrame = t;

    ctx.fillStyle = '#1A1D2E';
    ctx.fillRect(0, 0, size, size);

    var spinAngle = baseRotation + (t / 1000) * (2 * Math.PI * rpm);
    ctx.save();
    drawArc(ctx, spinAngle);
    ctx.restore();

    ctx.save();
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 0.8;
    ctx.lineCap = 'round';
    ctx.globalAlpha = 0.7;
    ctx.translate(cx, cy);
    ctx.rotate(baseRotation);
    ctx.translate(-cx, -cy);
    for (var i = 0; i < sparks.length; i++) {
      var s = sparks[i];
      ctx.beginPath();
      ctx.moveTo(s[0] * scale, s[1] * scale);
      ctx.lineTo(s[2] * scale, s[3] * scale);
      ctx.stroke();
    }
    ctx.restore();

    link.href = c.toDataURL('image/png');
    requestAnimationFrame(drawFavicon);
  }
  requestAnimationFrame(drawFavicon);
})();

// Clickjacking protection (frame-buster fallback — CSP meta tag cannot set frame-ancestors)
(function() {
  if (window.self !== window.top) {
    document.body.style.display = 'none';
    window.top.location = window.self.location;
  }
})();
