<?php
/**
 * Functions and definitions for Insights Ambiental WordPress Theme
 */

// Enqueue styles and scripts
function insights_ambiental_enqueue_assets() {
    // Enqueue theme styles
    wp_enqueue_style('insights-ambiental-style', get_stylesheet_uri(), array(), '1.0.0');
    
    // Add custom CSS for blog posts
    wp_add_inline_style('insights-ambiental-style', '
        body {
            font-family: system-ui, -apple-system, sans-serif;
            line-height: 1.6;
            color: #1f2937;
            background: #f9fafb;
        }
        .site-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 3rem 1rem;
        }
        .entry-content {
            background: white;
            padding: 3rem;
            border-radius: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .entry-content h2 {
            font-size: 2rem;
            font-weight: 700;
            color: #059669;
            margin-bottom: 1.5rem;
            margin-top: 2rem;
        }
        .entry-content h3 {
            font-size: 1.5rem;
            font-weight: 600;
            color: #047857;
            margin-bottom: 1rem;
            margin-top: 2rem;
        }
        .entry-content p {
            margin-bottom: 1rem;
            font-size: 1.125rem;
        }
        .entry-content img {
            max-width: 100%;
            height: auto;
            border-radius: 0.5rem;
            margin: 2rem 0;
        }
        @media (max-width: 768px) {
            .site-content {
                padding: 2rem 1rem;
            }
            .entry-content {
                padding: 1.5rem;
            }
            .entry-content h2 {
                font-size: 1.75rem;
            }
        }
    ');
}
add_action('wp_enqueue_scripts', 'insights_ambiental_enqueue_assets');

// Add theme support
function insights_ambiental_setup() {
    // Add theme support for post thumbnails
    add_theme_support('post-thumbnails');
    
    // Add theme support for title tag
    add_theme_support('title-tag');
    
    // Add theme support for HTML5
    add_theme_support('html5', array(
        'search-form',
        'comment-form',
        'comment-list',
        'gallery',
        'caption',
    ));
}
add_action('after_setup_theme', 'insights_ambiental_setup');

// Remove default WordPress header/footer styles that might conflict
function insights_ambiental_remove_default_styles() {
    // Remove default WordPress block styles if using block theme
    wp_dequeue_style('wp-block-library');
    wp_dequeue_style('wp-block-library-theme');
    wp_dequeue_style('wc-block-style');
}
add_action('wp_enqueue_scripts', 'insights_ambiental_remove_default_styles', 100);

