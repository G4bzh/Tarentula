<?php

/* include this file into the theme file functions.php */

/* Meta

dp_video_poster
dp_video_url
_yoast_wpseo_focuskw
_yoast_wpseo_focuskw_text_input
_yoast_wpseo_metadesc

*/

function my_postie_post_function($post) {

    /* Post title is et to TITLE¤VIDEO_URL */
    $ar_title = explode("¤",$post['post_title']);

    add_post_meta($post['ID'], 'dp_video_url', $ar_title[1]);
    add_post_meta($post['ID'], '_yoast_wpseo_focuskw', $ar_title[2]);
    add_post_meta($post['ID'], '_yoast_wpseo_focuskw_text_input', $ar_title[2]);
    add_post_meta($post['ID'], '_yoast_wpseo_metadesc', $ar_title[3]);
    $post['post_title']=$ar_title[0];
    $post['post_name']=$ar_title[0];



    /* Postie ImageTemplate should be set to custom with content: ¤{FILELINK}¤ */
    $ar_content = explode("¤",$post['post_content']);
    add_post_meta($post['ID'], 'dp_video_poster', $ar_content[1]);
    $post['post_content'] = $ar_content[0] . $ar_content[2];

    /* Views and likes */
    $views = rand(1,99)*1213;
    add_post_meta($post['ID'], 'views', $views);
    add_post_meta($post['ID'], 'likes', rand(123,$views/5));

    return $post;
}


add_filter('postie_post_before', 'my_postie_post_function');

?>