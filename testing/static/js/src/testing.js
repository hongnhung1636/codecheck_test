/* Javascript for TestingXBlock. */
function TestingXBlock(runtime, element) {
$(element).find('.send-button').bind('click', function() {
        var data = {
            'display_name': $(edit_display_name).context.value,
            'href':$(edit_href).context.value
        };
        $('.xblock-editor-error-message', element).html();
        $('.xblock-editor-error-message', element).css('display', 'none');
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
        $.post(handlerUrl, JSON.stringify(data)).done(function(response) {
            if (response.result === 'success') {
                window.location.reload(false);
            } else {
                $('.xblock-editor-error-message', element).html('Error: '+response.message);
                $('.xblock-editor-error-message', element).css('display', 'block');
            }
        });
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */
    });
}
