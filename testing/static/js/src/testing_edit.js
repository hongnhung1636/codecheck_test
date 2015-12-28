/**
 * Created by hongle on 12/26/15.
 */
function TestingXBlockEdit(runtime, element) {
    $('.save-button').bind('click', function() {
        var data = {
          'display_name': $('.display_name', element).val(),
          'href': $('.base-url', element).val()
        };
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
        $.post(handlerUrl, JSON.stringify(data)).complete(function() {
          window.location.reload(false);
        });
    });

  $('.cancel-button').bind('click', function() {
        runtime.notify('cancel', {});
  });
}