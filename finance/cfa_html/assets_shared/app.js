
function setViewMode(mode) {
  document.body.classList.remove('mode-bilingual', 'mode-vi-only', 'mode-en-only');
  document.body.classList.add(mode);
  localStorage.setItem('cfa_view_mode', mode);
  document.querySelectorAll('[data-mode-btn]').forEach(btn => {
    if (btn.getAttribute('data-mode-btn') === mode) {
      btn.classList.add('bg-indigo-600', 'text-white', 'shadow-xs');
      btn.classList.remove('text-slate-600', 'dark:text-slate-300');
    } else {
      btn.classList.remove('bg-indigo-600', 'text-white', 'shadow-xs');
      btn.classList.add('text-slate-600', 'dark:text-slate-300');
    }
  });
  const banner = document.getElementById('column-header-banner');
  if (banner) {
    banner.style.display = (mode === 'mode-bilingual') ? 'grid' : 'none';
  }
}

function toggleDark() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('cfa_dark', isDark ? '1' : '0');
}

function changeFontSize(delta) {
  let cur = parseInt(localStorage.getItem('cfa_font_size') || '16', 10);
  cur = Math.min(22, Math.max(13, cur + delta));
  document.documentElement.style.setProperty('--cfa-font-size', cur + 'px');
  localStorage.setItem('cfa_font_size', cur);
}

function toggleSidebar() {
  const sb = document.getElementById('cfa-sidebar');
  const ov = document.getElementById('cfa-sidebar-overlay');
  if (sb && ov) {
    sb.classList.toggle('-translate-x-full');
    ov.classList.toggle('hidden');
  }
}

function jumpToPdfPage(pageNum) {
  if (!pageNum) return;
  const el = document.getElementById('pdf-page-' + pageNum);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function openLightbox(src) {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-img');
  if (modal && img) {
    img.src = src;
    modal.classList.remove('hidden');
    modal.classList.add('flex');
  }
}

function closeLightbox() {
  const modal = document.getElementById('lightbox-modal');
  if (modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex');
  }
}

function toggleCompleted(pageKey) {
  let done = JSON.parse(localStorage.getItem('cfa_completed_items') || '{}');
  done[pageKey] = !done[pageKey];
  localStorage.setItem('cfa_completed_items', JSON.stringify(done));
  updateCompletedUI(pageKey);
}

function updateCompletedUI(pageKey) {
  let done = JSON.parse(localStorage.getItem('cfa_completed_items') || '{}');
  const btn = document.getElementById('btn-complete');
  if (btn) {
    if (done[pageKey]) {
      btn.innerHTML = '✓ Đã hoàn thành (Completed)';
      btn.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-emerald-600 text-white shadow-xs transition';
    } else {
      btn.innerHTML = '○ Đánh dấu hoàn thành';
      btn.className = 'px-3 py-1.5 rounded-lg text-xs font-semibold bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-emerald-500 hover:text-white transition';
    }
  }
}

document.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem('cfa_dark') === '1') {
    document.documentElement.classList.add('dark');
  }
  const savedSize = localStorage.getItem('cfa_font_size');
  if (savedSize) {
    document.documentElement.style.setProperty('--cfa-font-size', savedSize + 'px');
  }
  const savedMode = localStorage.getItem('cfa_view_mode') || 'mode-bilingual';
  setViewMode(savedMode);

  if (window.renderMathInElement) {
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false
    });
  }
});
