$(document).ready(function(){
    function trackScroll() {
        var scrolled = window.pageYOffset;
        var coords = document.documentElement.clientHeight;

        if (scrolled > coords) {
            goTopBtn.classList.add('back-to-top-show');
        }
        if (scrolled < coords) {
            goTopBtn.classList.remove('back-to-top-show');
        }
    }

    function backToTop() {
        if (window.pageYOffset > 0) {
            window.scrollBy(0, -80);
            setTimeout(backToTop, 0);
        }
    }
    function changeContentCheckbox(){
        if($('#content-has_uz').is(':checked')){
            $('.uz-field').prop('disabled', false);
        }
        else{
            $('.uz-field').prop('disabled', true);
        }
        if($('#content-has_ru').is(':checked')){
            $('.ru-field').prop('disabled', false);
        }
        else{
            $('.ru-field').prop('disabled', true);
        }
        if($('#content-has_en').is(':checked')){
            $('.en-field').prop('disabled', false);
        }
        else{
            $('.en-field').prop('disabled', true);
        }
    }

    $('#staticBackdrop').modal('show');
    $('#closeModalNew').click(function () {
        $('#staticBackdrop').modal('hide');
    })

    $('.nav').nav();
    $("#mobile-menu").on('click', function(){
        $('.nav-menu').removeClass('hidden-mobile');
    });

    $("#w1-container").find("[data-toggle=tooltip]").tooltip();

    $("#task-type_control").on('change', function(){
        console.log($(this).val());
        if($(this).val() == '1'){
            $("#task-term").prop('disabled', false);
            $("#task-term").val('1');
        }
        else{
            $("#task-term").prop('disabled', true);
            $("#task-term").val('0');
        }
    });

    $('#open-search-btn').on('click', function(){
        $('#search-form').css('display', 'block');
    });
    $('#close-search-btn').on('click', function(){
        $('#search-form').css('display', 'none');
    });
    $('#j-scroll-to-bottom').on('click', function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop: $($(this).attr('href')).offset().top}, 500, 'linear');
    });
    if($('#tiny-sliders').length){
        var slider = tns({
            container: '#tiny-sliders',
            mouseDrag: true,
            items: 1,
            slideBy: 'page',
            navPosition: 'bottom',
            preventScrollOnTouch: 'auto',
            autoplay: false,
            speed: 1000,
            autoplayTimeout: 20000,
            autoplayButtonOutput: false,
            controlsContainer: '#slider-controls',
        });
        var sliderChanged = function (info, eventName) {
            /*
            $('.slider-desc').each(function (){
                $(this).css('margin-bottom', '-200px');
                console.log('-200');
            });
            $('.slider-item').each(function () {
                console.log(this);
                var item = $(this).children().last().children().first().children().first().children().first().children().first().children().first().children().first();
                console.log(item);
                item.fadeIn("slow", function() {
                    $(this).css('margin-bottom', '0');
                });
            });*/
        }
        slider.events.on('transitionEnd', sliderChanged);
    }
    if($('#tiny-news').length){
        tns({
            container: '#tiny-news',
            mouseDrag: true,
            items: 1,
            gutter: 20,
            nav: false,
            slideBy: 'page',
            preventScrollOnTouch: 'auto',
            autoplayButtonOutput: false,
            controlsContainer: '#news-controls',
            responsive: {
                768: {
                    items: 2
                },
                992: {
                    items: 3
                },
            }
        });
    }
    if($('#tiny-announcements').length){
        tns({
            container: '#tiny-announcements',
            mouseDrag: true,
            items: 1,
            gutter: 20,
            nav: false,
            slideBy: 'page',
            preventScrollOnTouch: 'auto',
            autoplayButtonOutput: false,
            controlsContainer: '#announcements-controls',
            responsive: {
                768: {
                    items: 2
                },
                992: {
                    items: 3
                },
            }
        });
    }
    if($('#tiny-useful').length){
        tns({
            container: '#tiny-useful',
            mouseDrag: true,
            items: 1,
            gutter: 20,
            nav: false,
            slideBy: 'page',
            preventScrollOnTouch: 'auto',
            autoplayButtonOutput: false,
            controlsContainer: '#useful-controls',
            responsive: {
                768: {
                    items: 2
                },
                992: {
                    items: 4
                },
            }
        });
    }
    if($('#tiny-journals-recently').length){
        tns({
            container: '#tiny-journals-recently',
            mouseDrag: true,
            items: 1,
            gutter: 20,
            nav: false,
            slideBy: 'page',
            preventScrollOnTouch: 'auto',
            autoplayButtonOutput: false,
            controlsContainer: '#j-recently-controls',
            responsive: {
                576: {
                    items: 2
                },
                768: {
                    items: 3
                },
                992: {
                    items: 4
                },
                1341:{
                    items: 6
                }
            }
        });
    }
    if($('#tiny-conferences').length){
        tns({
            container: '#tiny-conferences',
            mouseDrag: true,
            items: 1,
            gutter: 20,
            nav: false,
            slideBy: 'page',
            preventScrollOnTouch: 'auto',
            autoplayButtonOutput: false,
            controlsContainer: '#conferences-controls',
            responsive: {
                768: {
                    items: 2
                },
                992: {
                    items: 3
                },
            }
        });
    }
    if($('#tiny-olympiads').length){
        tns({
            container: '#tiny-olympiads',
            mouseDrag: true,
            items: 1,
            gutter: 20,
            nav: false,
            slideBy: 'page',
            preventScrollOnTouch: 'auto',
            autoplayButtonOutput: false,
            controlsContainer: '#olympiads-controls',
            responsive: {
                768: {
                    items: 2
                },
                992: {
                    items: 3
                },
            }
        });
    }
    if($('#tiny-journals-popular').length){
        tns({
            container: '#tiny-journals-popular',
            mouseDrag: true,
            items: 1,
            gutter: 20,
            nav: false,
            slideBy: 'page',
            preventScrollOnTouch: 'auto',
            autoplayButtonOutput: false,
            controlsContainer: '#j-popular-controls',
            responsive: {
                576: {
                    items: 2
                },
                768: {
                    items: 3
                },
                992: {
                    items: 4
                },
                1341:{
                    items: 6
                }
            }
        });
    }
    if($("#div-article").length){
        $("#div-article").lightGallery({
            selector: '.view-gallery',
            thumbnail: false
        });
    }
    var $videoSrc;

    $('.video-btn').click(function() {
        $videoSrc = $(this).data( "src" );
    });


    $('#video-modal').on('shown.bs.modal', function (e) {
        $("#video").attr('src',$videoSrc + "?autoplay=1&amp;modestbranding=1&amp;showinfo=0" );
    });

    $('#video-modal').on('hide.bs.modal', function (e) {
        $("#video").attr('src',$videoSrc);
    });

    $window = $(window);
    var scrollAmount = 80;

    $(window).on('scroll', function(){
        if($(window).scrollTop()>=scrollAmount && !$('.header-sticky').hasClass('sticked')){
            $('.header-sticky').addClass('sticked');
        }
        else if($(window).scrollTop() < scrollAmount && $('.header-sticky').hasClass('sticked') && !$('.header-sticky').hasClass('no-remove')){
            $('.header-sticky').removeClass('sticked')
        }
    });
    if($('#index-numberlinks').length && $('#index-numberlinks').offset().top - $window.scrollTop() < 700){
        $('.count-from-to').countTo();
        $('.count-from-to').removeClass('count-from-to');
    }
    $("#project-print").on('click', function(){
        var p_window = window.open('', 'PRINT', 'height=595,width=842');

        p_window.document.write('<html><head><style>table {border-collapse:collapse;border-spacing:0;} .project-paper-top{visibility: hidden;} .project-qr-code{font-size: 14pt; line-height: 18pt}  p {margin-top: 0 !important; margin-bottom: 0 !important; font-size: 13pt; line-height: 17pt} .project-qr-code-bottom{font-size: 13pt;} .response-fb{float:right}</style>');
        p_window.document.write('</head><body><div style = "padding-left:8mm; padding-right: 8mm; padding-bottom: 16mm">');
        p_window.document.write(document.getElementById('project-paper').innerHTML);
        p_window.document.write('</div></body></html>');

        p_window.document.close();
        p_window.focus();

        p_window.print();
        p_window.close();
    });

    var goTopBtn = document.querySelector('.back-to-top');

    window.addEventListener('scroll', trackScroll);
    goTopBtn.addEventListener('click', backToTop);

    $('#content-has_uz').on('change', function(){
        changeContentCheckbox();
    });
    $('#content-has_ru').on('change', function(){
        changeContentCheckbox();
    });
    $('#content-has_en').on('change', function(){
        changeContentCheckbox();
    });

    changeContentCheckbox();
    setTimeout(function(){
        $("#pre-loader").addClass("loader-hide");
        wow = new WOW({
            boxClass:'wow',
            offset: 0,
            mobile: true,
            live: true
        })
        wow.init();
    }, 2000);

    lazyload();

    $('#staticBackdrop').modal('show');
    $('#closeModalNew').click(function () {
        $('#staticBackdrop').modal('hide');
    });

});