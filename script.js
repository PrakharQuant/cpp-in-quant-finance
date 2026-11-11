document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('pre').forEach(pre => {
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.textContent = 'Copy';
    btn.setAttribute('aria-label', 'Copy code');
    btn.addEventListener('click', () => {
      const code = pre.querySelector('code')?.innerText || pre.innerText;
      navigator.clipboard.writeText(code).then(() => {
        btn.textContent = 'Copied!';
        setTimeout(() => btn.textContent = 'Copy', 1500);
      }).catch(() => {
        btn.textContent = 'Failed';
        setTimeout(() => btn.textContent = 'Copy', 1500);
      });
    });
    pre.appendChild(btn);
  });

  // Smooth focus for accessibility
  document.querySelectorAll('a, button').forEach(el => {
    el.addEventListener('focus', () => el.style.outlineOffset = '2px');
  });
});
