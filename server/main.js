/*!
 * jQCloud Plugin for jQuery
 *
 * Version 1.0.4
 *
 * Copyright 2011, Luca Ongaro
 * Licensed under the MIT license.
 *
 * Date: 2013-05-09 18:54:22 +0200
 */
(function($) {
    "use strict";
    $.fn.jQCloud = function(word_array, options) {
        // Reference to the container element
        var $this = this;
        // Namespace word ids to avoid collisions between multiple clouds
        var cloud_namespace = $this.attr('id') || Math.floor((Math.random() * 1000000)).toString(36);

        // Default options value
        var default_options = {
            width: $this.width(),
            height: $this.height(),
            center: {
                x: ((options && options.width) ? options.width : $this.width()) / 2.0,
                y: ((options && options.height) ? options.height : $this.height()) / 2.0
            },
            shape: false, // It defaults to elliptic shape
            encodeURI: true,
            removeOverflowing: true
        };

        options = $.extend(default_options, options || {});

        // Add the "jqcloud" class to the container for easy CSS styling, set container width/height
        $this.addClass("jqcloud").width(options.width).height(options.height);

        // Container's CSS position cannot be 'static'
        if ($this.css("position") === "static") {
            $this.css("position", "relative");
        }

        var drawWordCloud = function() {
            // Helper function to test if an element overlaps others
            var hitTest = function(elem, other_elems) {
                // Pairwise overlap detection
                var overlapping = function(a, b) {
                    if (Math.abs(2.0 * a.offsetLeft + a.offsetWidth - 2.0 * b.offsetLeft - b.offsetWidth) < a.offsetWidth + b.offsetWidth) {
                        if (Math.abs(2.0 * a.offsetTop + a.offsetHeight - 2.0 * b.offsetTop - b.offsetHeight) < a.offsetHeight + b.offsetHeight) {
                            return true;
                        }
                    }
                    return false;
                };
                var i = 0;
                // Check elements for overlap one by one, stop and return false as soon as an overlap is found
                for (i = 0; i < other_elems.length; i++) {
                    if (overlapping(elem, other_elems[i])) {
                        return true;
                    }
                }
                return false;
            };


            var step = (options.shape === "rectangular") ? 18.0 : 2.0,
                already_placed_words = [],
                aspect_ratio = options.width / options.height;

            // Function to draw a word, by moving it in spiral until it finds a suitable empty place. This will be iterated on each word.
            var drawOneWord = function(index, word) {
                // Define the ID attribute of the span that will wrap the word, and the associated jQuery selector string
                var word_id = cloud_namespace + "_word_" + index,
                    word_selector = "#" + word_id,
                    angle = 6.28 * Math.random(),
                    radius = 0.0,

                    // Only used if option.shape == 'rectangular'
                    steps_in_direction = 0.0,
                    quarter_turns = 0.0,

                    custom_class = "",
                    inner_html = "",
                    word_span;

                // Extend word html options with defaults
                word.html = $.extend(word.html, {
                    id: word_id
                });



                word_span = $('<span>').attr(word.html);

                word_span.append(word.text);


                $this.append(word_span);

                var width = word_span.width(),
                    height = word_span.height(),
                    left = options.center.x - width / 2.0,
                    top = options.center.y - height / 2.0;

                // Save a reference to the style property, for better performance
                var word_style = word_span[0].style;
                word_style.position = "absolute";
                word_style.left = left + "px";
                word_style.top = top + "px";

                while (hitTest(word_span[0], already_placed_words)) {
                    // option shape is 'rectangular' so move the word in a rectangular spiral
                    if (options.shape === "rectangular") {
                        steps_in_direction++;
                        if (steps_in_direction * step > (1 + Math.floor(quarter_turns / 2.0)) * step * ((quarter_turns % 4 % 2) === 0 ? 1 : aspect_ratio)) {
                            steps_in_direction = 0.0;
                            quarter_turns++;
                        }
                        switch (quarter_turns % 4) {
                            case 1:
                                left += step * aspect_ratio + Math.random() * 2.0;
                                break;
                            case 2:
                                top -= step + Math.random() * 2.0;
                                break;
                            case 3:
                                left -= step * aspect_ratio + Math.random() * 2.0;
                                break;
                            case 0:
                                top += step + Math.random() * 2.0;
                                break;
                        }
                    } else { // Default settings: elliptic spiral shape
                        radius += step;
                        angle += (index % 2 === 0 ? 1 : -1) * step;

                        left = options.center.x - (width / 2.0) + (radius * Math.cos(angle)) * aspect_ratio;
                        top = options.center.y + radius * Math.sin(angle) - (height / 2.0);
                    }
                    word_style.left = left + "px";
                    word_style.top = top + "px";
                }


                already_placed_words.push(word_span[0]);


            };

            var drawOneWordDelayed = function(index) {
                index = index || 0;

                if (index < word_array.length) {
                    drawOneWord(index, word_array[index]);
                    (function() {
                        drawOneWordDelayed(index + 1);
                    })()
                } else {
                    if ($.isFunction(options.afterCloudRender)) {
                        options.afterCloudRender.call($this);
                    }
                }
            };


            $.each(word_array, drawOneWord);
            if ($.isFunction(options.afterCloudRender)) {
                options.afterCloudRender.call($this);
            }

        };

        // Delay execution so that the browser can render the page before the computatively intensive word cloud drawing
        (function() {
            drawWordCloud();
        })();
        return $this;
    };
})(jQuery);


webSocket = new WebSocket('ws://localhost:8765');
webSocket.onopen = event => {
    console.info('connected')
}

webSocket.onmessage = event => {
            console.info(`Received ${event.data}`)

            switch(event.data) {
                case 'focus':
                    document.getElementById('word-cloud').classList.remove('blurred')
                    document.getElementById('word-cloud').classList.remove('hidden')
                    break;
                case 'blur':
                    document.getElementById('word-cloud').classList.add('blurred')
                    document.getElementById('word-cloud').classList.remove('hidden')
                    break;
                case 'hide':
                    document.getElementById('word-cloud').classList.add('hidden')
                    break;
            }
            
            
        }

var word_arrays = [];

for (i = 0; i < 200; i++) {
    word_arrays.push({
        text: Math.floor(Math.random() * 10),
    })
}

var removeAllChildNodes = function(parent) {
    while (parent.firstChild) {
        parent.removeChild(parent.firstChild);
    }
}

input = 0;


var keydownHandler = (event) => {
    switch (event.key) {
        case "Enter":
            // remove event listener
            removeEventListener('keydown', keydownHandler)

            // Send counted numbers event
            actual = word_arrays.reduce((acc, input) => {
                if (input.text === 8) {
                    return acc + 1
                } else {
                    return acc
                }
            }, 0)

            console.log("Task: ", JSON.stringify({
                counted: input,
                actual: actual,
                errorRatio: Math.abs(actual-input) / Math.max(actual, input) * 100
            }))
            // webSocket.send(JSON.toString({counted: input, actual: noOfEights}))

            input = 0

            // Generate new task
            word_arrays = [];
            for (i = 0; i < 200; i++) {
                word_arrays.push({
                    text: Math.floor(Math.random() * 10),
                })
            }
            removeAllChildNodes(document.getElementById('word-cloud'))
            $("#word-cloud").jQCloud(word_arrays, {
                width: 500,
                height: 350,
                afterCloudRender: afterCloudRender
            });
            break;
        default:
            if (RegExp('\\d+$').test(event.code)) {
                input = input * 10
                input += parseInt(event.key)
            }
            break;
    }

}

var afterCloudRender = () => {
    // add keyboard event listener for count input
    document.addEventListener('keydown', keydownHandler)
}


$("#word-cloud").jQCloud(word_arrays, {
    width: 500,
    height: 350,
    afterCloudRender: afterCloudRender
});