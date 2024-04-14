/* -----------------------------------------------------------------------------



File:           JS Core
Version:        1.0
Last change:    00/00/00 
-------------------------------------------------------------------------------- */
(function() {

	"use strict";

	var RexLaw = {
		init: function() {
			this.Basic.init();  
		},

		Basic: {
			init: function() {

				this.preloader();
				this.BackgroundImage();
				this.StickyHeader();
				this.MobileMenu();
				this.Animation();
				this.SideInner();
				this.scrollTop();
				this.MianSlider();
				this.blogSlider();
				this.CirleProgress();
				this.serviceSlide();
				this.bannerParalax();
				this.PortfolioSlide();
				this.TestimonialSlider();
				this.counterUp();
				this.GoogleMap();
				this.videoBox();
				this.AwardSlide();
				this.EstimateItem();
				this.CaseFilter();
				this.faqShadow();
			},
			preloader: function (){
				jQuery(window).on('load', function(){
					jQuery('#preloader').fadeOut('slow',function(){jQuery(this).remove();});
				});
			},
			BackgroundImage: function (){
				$('[data-background]').each(function() {
					$(this).css('background-image', 'url('+ $(this).attr('data-background') + ')');
				});
			},
			StickyHeader: function (){
				jQuery(window).on('scroll', function() {
					if (jQuery(window).scrollTop() > 250) {
						jQuery('.main_header').addClass('menu-bg-overlay')
					} else {
						jQuery('.main_header').removeClass('menu-bg-overlay')
					}
				})
			},
			SideInner: function (){
				$('.open_side_area').on("click", function() {
					$('.wide_side_inner').toggleClass("wide_side_on");
				});
				$('.open_side_area').on('click', function () {
					$('body').toggleClass('body_overlay_on');
				});
			},
			scrollTop: function (){
				$(window).on("scroll", function() {
					if ($(this).scrollTop() > 250) {
						$('.scrollup').fadeIn();
					} else {
						$('.scrollup').fadeOut();
					}
				});

				$('.scrollup').on("click", function()  {
					$("html, body").animate({
						scrollTop: 0
					}, 800);
					return false;
				});
			},
			MobileMenu: function (){
				$('.open_mobile_menu').on("click", function() {
					$('.mobile_menu_wrap').toggleClass("mobile_menu_on");
					return false;
				});
				$('.open_mobile_menu').on('click', function () {
					$('body').toggleClass('mobile_menu_overlay_on');
					return false;
				});
				$(document).on('click', ".mobile_menu_wrap ul li.dropdown > a", function(event) {
					$(this).parent().find(".dropdown-menu").slideToggle("slow");
					return false;
				});
			},
			Animation: function (){
				if($('.wow').length){
					var wow = new WOW(
					{
						boxClass:     'wow',
						animateClass: 'animated',
						offset:       0,
						mobile:       true,
						live:         true
					}
					);
					wow.init();
				}
			},
			MianSlider: function (){
				jQuery('#slider_id').owlCarousel({
					items: 1,
					loop: true,
					nav: true,
					dots: false,
					autoplay: false,
					navSpeed: 800,
					smartSpeed: 1000,
					animateOut: 'fadeOut',
					navText:["<i class='fas fa-arrow-left'></i>","<i class='fas fa-arrow-right'></i>"],
				});
			},
			blogSlider: function (){
				jQuery('#blod_slide').owlCarousel({
					items: 1,
					loop: true,
					nav: true,
					dots: false,
					autoplay: false,
					navSpeed: 800,
					smartSpeed: 1000,
					animateOut: 'fadeOut',
					navText:["<i class='fas fa-arrow-left'></i>","<i class='fas fa-arrow-right'></i>"],
				});
			},
			CirleProgress: function (){
				if($('.progress_area').length){
					;(function() {
						var proto = $.circleProgress.defaults,
						originalDrawEmptyArc = proto.drawEmptyArc;

						proto.emptyThickness = 5; 
						proto.drawEmptyArc = function(v) {
							var oldGetThickness = this.getThickness, 
							oldThickness = this.getThickness(),
							emptyThickness = this.emptyThickness || _oldThickness.call(this),
							oldRadius = this.radius,
							delta = (oldThickness - emptyThickness) / 2;

							this.getThickness = function() {
								return emptyThickness;
							};

							this.radius = oldRadius - delta;
							this.ctx.save();
							this.ctx.translate(delta, delta);

							originalDrawEmptyArc.call(this, v);

							this.ctx.restore();
							this.getThickness = oldGetThickness;
							this.radius = oldRadius;
						};
					})();
					$('.progress_area').circleProgress({
						emptyThickness: 2,
						size: 75,
						thickness: 5,
						lineCap: 'round',
						fill: {
							gradient: ['#b89b5e', ['#b89b5e', 0.7]],
							gradientAngle: Math.PI * -0.3
						}  
					});

					$('.first.progress_area').circleProgress({
						value: .65,
						thickness: 6,
						emptyFill: '#f0f0f0',
					}).on('circle-animation-progress', function(event, progress) {
						$(this).find('strong').html(Math.round(65 * progress) + '<span>%</span>');
					});
					$('.secound.progress_area').circleProgress({
						value: .5,
						thickness: 6,
						emptyFill: '#f0f0f0',
					}).on('circle-animation-progress', function(event, progress) {
						$(this).find('strong').html(Math.round(50 * progress) + '<span>%</span>');
					});
					var el = $('.progress_area'),
					inited = false;
					el.appear({ force_process: true });

					el.on('appear', function() {
						if (!inited) {
							el.circleProgress();
							inited = true;
						}
					});
				};
			},
			serviceSlide: function (){
				$('#service_slide').owlCarousel({
					margin:30,
					responsiveClass:true,
					nav: true,
					dots: false,
					loop:true,
					autoplay: false,
					navText:["<i class='fas fa-arrow-left'></i>","<i class='fas fa-arrow-right'></i>"],
					smartSpeed: 1000,
					responsive:{
						0:{
							items:1,
						},
						400:{
							items:1,
						},
						600:{
							items:2,
						},
						700:{
							items:2,
						},
						1000:{
							items:3,

						}
					},
				})
			},
			bannerParalax: function (){
				$('.background_parallax').jarallax({
					speed: 0.3,
				});
			},
			PortfolioSlide: function (){
				$('#portfolio_slideid').owlCarousel({
					margin:30,
					responsiveClass:true,
					nav: true,
					dots: false,
					loop:true,
					autoplay: false,
					navText:["<i class='fas fa-arrow-left'></i>","<i class='fas fa-arrow-right'></i>"],
					smartSpeed: 1000,
					responsive:{
						0:{
							items:1,
						},
						400:{
							items:1,
						},
						600:{
							items:2,
						},
						700:{
							items:2,
						},
						1000:{
							items:4,

						}
					},
				})
			},
			TestimonialSlider: function (){
				jQuery('#testimonial_slide').owlCarousel({
					items: 1,
					margin: 30,
					loop: true,
					nav: false,
					dots: true,
					smartSpeed: 1000,
					autoplay: false,
				});
			},
			counterUp: function (){
				if ($(".odometer").length) {
					$('.odometer').appear();
					$(document.body).on('appear', '.odometer', function(e) {
						var odo = $(".odometer");
						odo.each(function() {
							var countNumber = $(this).attr("data-count");
							$(this).html(countNumber);
						});
					});
				}
			},
			videoBox: function (){
				jQuery('.video_box').magnificPopup({
					disableOn: 200,
					type: 'iframe',
					mainClass: 'mfp-fade',
					removalDelay: 160,
					preloader: false,
					fixedContentPos: false,
				});
			},
			AwardSlide: function (){
				$('#award_list_slide').owlCarousel({
					margin: 30,
					loop:true,
					responsiveClass:true,
					nav: false,
					dots: false,
					autoplay: true,
					smartSpeed: 1000,
					responsive:{
						0:{items:1},
						480:{items:1},
						600:{items:2},
						800:{items:3},
						1024:{items:4}
					}
				})
			},
			EstimateItem: function (){
				if ($("#estimate_scale").length) {
					var pipsSlider = document.getElementById('estimate_scale');
					noUiSlider.create(pipsSlider, {
						range: {
							min: 1000,
							max: 6000
						},
						start: [3000],
						pips: {mode: 'count', values: 6},		
					});
				};
			},
			CaseFilter:  function (){
				jQuery(window).on('load', function(){
					$('.filtr-container');
					var filterizd = $('.filtr-container');

					if(filterizd.length) {
						filterizd.filterizr({

						});
						$('.filtr-button').on('click', function() {

							$('.filtr-button.filtr-active').removeClass('filtr-active');
							$(this).addClass('filtr-active');
						});
					}
				});
			},
			faqShadow: function (){
				$(document).on('click', '.ei-faq', function(){
					$(this).addClass('faq_shadow').siblings().removeClass('faq_shadow')
				}) 
				$(document).on('click', '.faq_topic ul li', function(){
					$(this).addClass('faq_on').siblings().removeClass('faq_on')
				}) 
			},
			GoogleMap: function (){
				function isMobile() { 
					return ('ontouchstart' in document.documentElement);
				}
				function init_gmap() {
					if ( typeof google == 'undefined' ) return;
					var options = {
						center: [40.712784,-74.005941],
						zoom: 10,
						styles: [
						{
							"featureType": "all",
							"elementType": "geometry.fill",
							"stylers": [
							{
								"weight": "2.00"
							}
							]
						},
						{
							"featureType": "all",
							"elementType": "geometry.stroke",
							"stylers": [
							{
								"color": "#9c9c9c"
							}
							]
						},
						{
							"featureType": "all",
							"elementType": "labels.text",
							"stylers": [
							{
								"visibility": "on"
							}
							]
						},
						{
							"featureType": "landscape",
							"elementType": "all",
							"stylers": [
							{
								"color": "#f2f2f2"
							}
							]
						},
						{
							"featureType": "landscape",
							"elementType": "geometry.fill",
							"stylers": [
							{
								"color": "#ffffff"
							}
							]
						},
						{
							"featureType": "landscape.man_made",
							"elementType": "geometry.fill",
							"stylers": [
							{
								"color": "#ffffff"
							}
							]
						},
						{
							"featureType": "poi",
							"elementType": "all",
							"stylers": [
							{
								"visibility": "off"
							}
							]
						},
						{
							"featureType": "road",
							"elementType": "all",
							"stylers": [
							{
								"saturation": -100
							},
							{
								"lightness": 45
							}
							]
						},
						{
							"featureType": "road",
							"elementType": "geometry.fill",
							"stylers": [
							{
								"color": "#eeeeee"
							}
							]
						},
						{
							"featureType": "road",
							"elementType": "labels.text.fill",
							"stylers": [
							{
								"color": "#7b7b7b"
							}
							]
						},
						{
							"featureType": "road",
							"elementType": "labels.text.stroke",
							"stylers": [
							{
								"color": "#ffffff"
							}
							]
						},
						{
							"featureType": "road.highway",
							"elementType": "all",
							"stylers": [
							{
								"visibility": "simplified"
							}
							]
						},
						{
							"featureType": "road.arterial",
							"elementType": "labels.icon",
							"stylers": [
							{
								"visibility": "off"
							}
							]
						},
						{
							"featureType": "transit",
							"elementType": "all",
							"stylers": [
							{
								"visibility": "off"
							}
							]
						},
						{
							"featureType": "water",
							"elementType": "all",
							"stylers": [
							{
								"color": "#46bcec"
							},
							{
								"visibility": "on"
							}
							]
						},
						{
							"featureType": "water",
							"elementType": "geometry.fill",
							"stylers": [
							{
								"color": "#c8d7d4"
							}
							]
						},
						{
							"featureType": "water",
							"elementType": "labels.text.fill",
							"stylers": [
							{
								"color": "#070707"
							}
							]
						},
						{
							"featureType": "water",
							"elementType": "labels.text.stroke",
							"stylers": [
							{
								"color": "#ffffff"
							}
							]
						}
						],
						mapTypeControl: true,
						mapTypeControlOptions: {
							style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
						},
						navigationControl: true,
						scrollwheel: false,
						streetViewControl: true,
					}
					if (isMobile()) {
						options.draggable = false;
					}
					$('#googleMaps').gmap3({
						map: {
							options: options
						},
						marker: {
							latLng: [40.712776,-74.005974],
							options: { icon: 'assets/img/map.png' }

						}
					});
				}
				init_gmap();
			},
		}
	}
	jQuery(document).ready(function (){
		RexLaw.init();
	});

})();