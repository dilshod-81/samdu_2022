/**
 * Created by Azamat Mirvosiqov on 29.01.2015.
 */

var curUrl = window.location.href;
var arCurUrl = curUrl.split('/');
var noImageTitle = 'Rasmsiz';
var setImageTitle = 'Rasmli';
switch (arCurUrl[3]){
    case 'uz':
        noImageTitle = 'Rasmsiz';
        setImageTitle = 'Rasmli';
        break;
    case 'ru':
        noImageTitle = 'Р‘РµР· РєР°СЂС‚РёРЅРєРё';
        setImageTitle = 'РЎ РєР°СЂС‚РёРЅРєРѕР№';
        break;
    case 'en':
        noImageTitle = 'Without a picture';
        setImageTitle = 'With a picture';
        break;
}

var min = 14,
    max = 24;
var minzoom = 0,
    maxzoom = 4;

function makeNormal() {
    $('html').removeClass('blackAndWhite blackAndWhiteInvert');
    $.removeCookie('specialView', {path: '/'});
}

function makeBlackAndWhite() {
    makeNormal();
    $('html').addClass('blackAndWhite');
    $.cookie("specialView", 'blackAndWhite', {path: '/'});
}

function makeBlackAndWhiteDark() {
    makeNormal();
    $('html').addClass('blackAndWhiteInvert');
    $.cookie("specialView", 'blackAndWhiteInvert', {path: '/'});
}

function makeSetImage() {
    $('html').removeClass( "noImage" );
    //$('.spcImage').removeClass( "spcSetImage" );
    $('.spcNoImage').removeClass( "spcSetImage" );
    $('.spcNoImage').attr('data-original-title', setImageTitle);
    $('.spcNoImage').attr('title', setImageTitle);
    $.removeCookie('specialViewImage', {path: '/'});
}

function makeNoImage() {
    $('html').stop().addClass( "noImage" );
    $('.spcNoImage').addClass( "spcSetImage" );
    $('.spcNoImage').attr('data-original-title', noImageTitle);
    $('.spcNoImage').attr('title', noImageTitle);
    $.cookie("specialViewImage", 'noImage', {path: '/'});
}

function offImages(){
    if ($.cookie("specialViewImage") == 'noImage'){
        makeSetImage();
    } else {
        makeNoImage();
    }
}

function setFontSize(size) {
    if (size < min) {
        size = min;
    }
    if (size > max) {
        size = max;
    }
    $('.editable-font').css({'font-size': parseInt(size) + 'px'});
    $(".editable-font").each(function(){
        var n_size = parseInt($(this).data('font')) - parseInt(min) + parseInt(size);
        console.log(n_size);
        $(this).css({'font-size': parseInt(n_size) + 'px'});
    });
}
function setzoomSizer(size) {
    if (size < minzoom) {
        size = minzoom;
    }
    if (size > maxzoom) {
        size = maxzoom;
    }
    $('body').css({
        // 'zoom': '1.' + parseInt(size),
        // '-ms-zoom': '1.' + parseInt(size),
        // '-webkit-zoom': '1.' + parseInt(size),
        // '-moz-zoom': '1.' + parseInt(size),
        // '-o-zoom': '1.' + parseInt(size),
        '-webkit-transform': 'scale(1.0' + parseInt(size) + ')',
        '-moz-transform': 'scale(1.0' + parseInt(size) + ')',
        '-ms-transform': 'scale(1.0' + parseInt(size) + ')',
        'transform': 'scale(1.0' + parseInt(size) + ')',
        '-webkit-transform-origin': 'top center',
        '-moz-transform-origin': 'top center',
        '-ms-transform-origin': 'top center',
        'transform-origin': 'top center',
        // '-webkit-transform': 'scale(1.'+parseInt(size)+')',
        // 'transform': "scale(1."+parseInt(size)+")",
        // 'margin-top': ""+ (parseInt(size) + 20) +"%",


    });
}
function saveFontSize(size) {
    $.cookie("fontSize", size, {path: '/'});
}
function savezoomSizer(size) {
    $.session("zoomSizer", size, {path: '/'});
}
function setNarrator() {
    $('head').append($('<script type="text/javascript"><\/script>').attr('src', '/js/narrator.js'));
    console.log($('head'));
    narrator.init();
    $.cookie("narrator", 'on', {path: '/'});
    if (typeof($.cookie("speechVolume")) == 'undefined') {
        $("#speechVolume").slider('value', 100);
        $('#speechOptions .sliderText .range').text(100);
    } else {
        var speechVolume = $.cookie("speechVolume");
        $("#speechVolume").slider('value', speechVolume);
        $('#speechOptions .sliderText .range').text(speechVolume);
    }
}

function unsetNarrator() {
    $.cookie("narrator", null, { path: '/' });
    $('#speech').remove();
    removeJsCssFile('narrator.js', 'js');
}

function saveSpeechVolume(val) {
    if (val > 100 || val < 25) {
        val = 100;
    }
    narrator.setVolume(val);
    $.cookie("speechVolume", val, {path: '/'});
}

$(document).ready(function () {
    var appearance = $.cookie("specialView");
    switch (appearance) {
        case 'blackAndWhite':
            makeBlackAndWhite();
            break;
        case 'blackAndWhiteInvert':
            makeBlackAndWhiteDark();
            break;
    }
    var noimage = $.cookie("specialViewImage");
    switch (noimage) {
        case 'noImage':
            makeNoImage();
            break;
        case 'setImage':
            makeSetImage();
            break;
    }

    $('.no-propagation').click(function (e) {
        e.stopPropagation();
    });

    $('.appearance .spcNormal').click(function () {
        makeNormal();
    });
    $('.appearance .spcWhiteAndBlack').click(function () {
        makeBlackAndWhite();

    });
    $('.appearance .spcDark').click(function () {
        makeBlackAndWhiteDark();
    });

    $('.appearance .spcNoImage').click(function () {
        offImages();
    });


    $('#speechSwitcher').change(function () {
        if (this.checked) {
            var narratorStatus = $.cookie("narrator");
            $('#speechOptions').slideDown(100);
            setNarrator();
            if (narratorStatus != 'on')
                narrator.speak($(this).attr('title'));
            $(".speech").stop().animate({opacity:1}, "fast").addClass('speechHover');
        } else {
            $('#speechOptions').slideUp(100);
            unsetNarrator();
            $(".speech").stop().removeClass('speechHover');
        }
    });

    $('#f-size').on('input', function(){
        var val = $('#f-size').val();
        setFontSize(val);
        $('#f-size-val').html(val);
        saveFontSize(val);
    });

    var fontSize = $.cookie("fontSize");
    if (typeof(fontSize) != 'undefined') {
        $("#f-size").val(fontSize);
        setFontSize(fontSize);
        $('#f-size-val').html(fontSize);
    }
    $('#z-size').on('input', function(){
        var val = $('#z-size').val();
        setzoomSizer(val);
        $('#z-size-val').html(val);
    });

    var zoomSize = $.cookie("zoomSizer");
    if (typeof(zoomSize) != 'undefined') {
        $("#z-size").val(zoomSize);
        setzoomSizer(fontSize);
        $('#z-size-val').html(zoomSize);
        savezoomSizer(val);
    }

    Mousetrap.bind(['shift+return'], function() {
        $('#speechSwitcher').prop('checked', !$('#speechSwitcher').prop('checked'));
        $('#speechSwitcher').trigger('change');
        return false;
    });

    if ($.cookie("narrator") == 'on' && typeof($.cookie("narrator")) != 'undefined'){
        $('#speechSwitcher').prop('checked', true);
        $('#speechSwitcher').trigger('change');
        var speechVolume = $.cookie("speechVolume");
        if (typeof(speechVolume) != 'undefined') {
            $("#speechVolume").slider('value', speechVolume);
            $('#speechOptions .sliderText .range').text(speechVolume);
        }
        if (typeof(speechNotification) != 'undefined'){
            narrator.speak(speechNotification);
        }

        Mousetrap.bind(['ctrl+shift'], function() {
            narrator.stop();
            $('#speechArea').removeClass('narratorBox');
            return false;
        });

        Mousetrap.bind(['ctrl+alt'], function() {
            if (typeof($('#speechArea')) != 'undefined'){
                $('#speechArea').addClass('narratorBox');
                $('#speechArea').append('<div class="loading"></div>');
                narrator.speak($('#speechArea').text());
            }
            return false;
        });
    }
});