/*
 * goNotification (jQuery)
 * version: 0.1.1 (28/04/2014)
 * author: @tiagoitsme
 * homepage: http://tiagoitsme.github.io/goNotification - http://talk.tiagoits.me
 *
 * Licensed under the MIT license
 *      http://www.opensource.org/licenses/mit-license.php

 * Ghost-style notification plugin (Ghost.org)
 *
 */

;(function ( $, window, document, undefined ) {
    
    $.goNotification = function(message, options)
    {
        /* defaults */

        var types = ['success','warning','loading','info','error'],
            
            settings = $.extend({
                type: (typeof options === 'string' && $.inArray(options, types) != '-1' ? options : 'success'),
                position: 'bottom left',
                timeout: 4000,
                animation: 'fade',
                animationSpeed: 'slow',
                allowClose: true,
                shadow: false,
                stripes: false,
                onClose: function() {},
                onStart: function() {}
            }, options);

            if(settings.type == 'loading'){
                message = (message.length > 0 ? message : 'Loading...');
                var $loading = true;
            }

            var $animation = {};
            
            if(settings.animation == 'fade'){
                $animation['opacity'] = "toggle";
            } else if(settings.animation == 'slide' || settings.animation){
                $animation['height'] = "toggle";
            }

        /* end */

        settings.onStart.call(this);

        if($('[class="js-go-notification ' + settings.position + '"]').length == 0){

            $aside = '<aside class="js-go-notification ' + settings.position + '"></aside>';
            $('body').append($aside);

        }

        _makeid = function()
        {
            var text = "";
            var possible = "0123456789";

            for( var i=0; i < 16; i++ )
                text += possible.charAt(Math.floor(Math.random() * possible.length));

            return text;
        };

        var notification_id = 'go-' + _makeid();

        $holder = $('[class="js-go-notification ' + settings.position + '"]');
        $template = '<article id="' + notification_id + '" class="notification ' + settings.type + ' ' + (settings.shadow ? 'shadow' : '') + ' ' + (settings.stripes ? 'stripes' : '') + '"><section>' + message + ' ' + (settings.allowClose && !$loading ? '<i class="fa fa-times-circle"></i>' : '' ) + '</section></article>';
        $holder.append($template);

        $notification = $("#" + notification_id);
        $notification.animate($animation, settings.animationSpeed);

        /* functions */

        var $close = $("#" + notification_id + ' section i'),
            
            _timer = function(time, update, complete){
                var start = new Date().getTime();
                var interval = setInterval(function() {
                    var now = time-(new Date().getTime()-start);
                    if( now <= 0) {
                        clearInterval(interval);
                        complete();
                    }
                    else update(Math.floor(now/1000));
                }, 100);
            },
            
            _close = function()
            {
                settings.onClose.call(this);

                $("#" + notification_id).animate($animation, settings.animationSpeed, function(){
                    $(this).remove();

                    if($holder.find('article').length == 0){
                        $holder.remove();
                    }
                });
            };

        /* binds */

        $close.on("click", function(){
            _close();
        });

        if(!$loading){
            
            if(settings.timeout){
                _timer( settings.timeout, function(sec){ /* sec returns the seconds remaining */ }, function(){ _close() });
            }   

        };
        
        return {
            close: _close
        }; 
    };

})( jQuery, window, document );