<!doctype html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo('charset'); ?>" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1" />
  <link rel="icon" type="image/png" href="https://www.insightsambiental.com.br/images/favicon.png" />
  <link rel="apple-touch-icon" href="https://www.insightsambiental.com.br/images/favicon.png" />
  <?php wp_head(); ?>
  <style>
    /* Updated: Logo size adjusted to match main site - v1.1.0 */
    /* Top Bar Styles */
    .top-bar {
      background-color: #047857;
      padding: 0.5rem 0;
      display: flex;
      justify-content: flex-end;
      align-items: center;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 60;
    }
    .top-bar-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1rem;
      width: 100%;
      display: flex;
      justify-content: flex-end;
      gap: 1rem;
    }
    .social-icons {
      display: flex;
      gap: 0.75rem;
      align-items: center;
    }
    .social-icon {
      width: 20px;
      height: 20px;
      color: white;
      transition: opacity 0.2s;
    }
    .social-icon:hover {
      opacity: 0.8;
    }
    .social-icon svg {
      width: 100%;
      height: 100%;
      fill: currentColor;
    }
    /* Header Styles */
    .site-header {
      position: fixed;
      top: 32px;
      left: 0;
      right: 0;
      z-index: 50;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .main-header {
      background-color: #d8dacd;
      background-image: url(https://www.insightsambiental.com.br/images/logo_texture.png);
      background-repeat: repeat;
      background-size: auto;
    }
    .header-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1rem;
    }
    .header-content {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 96px;
      padding: 1rem 0;
    }
    .header-logo {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      transition: opacity 0.2s;
    }
    .header-logo:hover {
      opacity: 0.9;
    }
    .header-logo img {
      max-height: 60px;
      height: auto;
      width: auto;
      object-fit: contain;
    }
    .header-nav {
      display: none;
    }
    @media (min-width: 1024px) {
      .header-nav {
        display: flex;
        align-items: center;
        gap: 1.5rem;
      }
    }
    .nav-link {
      font-size: 0.875rem;
      font-weight: 500;
      color: #1f2937;
      text-decoration: none;
      transition: color 0.2s;
    }
    .nav-link:hover {
      color: #059669;
    }
    .nav-link.active {
      color: #059669;
    }
    .nav-button {
      background-color: #059669;
      color: white;
      padding: 0.5rem 1rem;
      border-radius: 0.5rem;
      border: none;
      font-size: 0.875rem;
      font-weight: 500;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: background-color 0.2s;
    }
    .nav-button:hover {
      background-color: #047857;
    }
    body {
      padding-top: 128px;
    }
    @media (max-width: 768px) {
      .top-bar {
        display: none;
      }
      .site-header {
        top: 0;
      }
      body {
        padding-top: 80px;
      }
      .header-content {
        height: 80px;
      }
      .header-logo img {
        max-height: 60px;
        height: auto;
      }
    }
  </style>
</head>
<body <?php body_class(); ?>>
  <!-- Header -->
  <header class="site-header">
    <!-- Top Bar with Social Icons -->
    <div class="top-bar">
      <div class="top-bar-container">
        <div class="social-icons">
          <a href="https://www.linkedin.com/company/insights-ambiental" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
            </svg>
          </a>
          <a href="https://www.instagram.com/insightsambiental" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Instagram">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/>
            </svg>
          </a>
          <a href="https://wa.me/5551993308012" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="WhatsApp">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
            </svg>
          </a>
        </div>
      </div>
    </div>
    <!-- Main Header -->
    <div class="main-header">
      <div class="header-container">
        <div class="header-content">
          <a href="https://www.insightsambiental.com.br/" class="header-logo">
            <img src="https://www.insightsambiental.com.br/images/logo_h.png" alt="Insights Ambiental" />
          </a>
          <nav class="header-nav">
            <a href="https://www.insightsambiental.com.br/" class="nav-link">Início</a>
            <a href="https://www.insightsambiental.com.br/#sobre" class="nav-link">Sobre</a>
            <a href="https://www.insightsambiental.com.br/#servicos" class="nav-link">Serviços</a>
            <a href="https://www.insightsambiental.com.br/#areas" class="nav-link">Áreas de Atuação</a>
            <a href="https://www.insightsambiental.com.br/artigos" class="nav-link <?php echo (is_home() || is_single() || is_category() || is_tag()) ? 'active' : ''; ?>">Artigos</a>
            <a href="https://www.insightsambiental.com.br/#contato" class="nav-button">Contato</a>
          </nav>
        </div>
      </div>
    </div>
  </header>

