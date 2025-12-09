<?php
/**
 * Main template file
 */
get_header();
?>

<main class="site-content">
    <?php if (have_posts()) : ?>
        <?php while (have_posts()) : the_post(); ?>
            <article id="post-<?php the_ID(); ?>" <?php post_class('entry-content'); ?>>
                <header class="entry-header">
                    <h1 class="entry-title"><?php the_title(); ?></h1>
                    <?php if (has_post_thumbnail()) : ?>
                        <div class="entry-thumbnail">
                            <?php the_post_thumbnail('large'); ?>
                        </div>
                    <?php endif; ?>
                </header>
                
                <div class="entry-content">
                    <?php the_content(); ?>
                </div>
            </article>
        <?php endwhile; ?>
    <?php else : ?>
        <p>Nenhum post encontrado.</p>
    <?php endif; ?>
</main>

<?php
get_footer();
?>

