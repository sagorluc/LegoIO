$(function(){
   	
   	'use strict';


   	// SLIDER
   

    $(document).ready(function() {
     
      $("#slider").owlCarousel({
     
          navigation : true, // Show next and prev buttons
          slideSpeed : 300,
          paginationSpeed : 400,
          singleItem:true
     
          // "singleItem:true" is a shortcut for:
          // items : 1, 
          // itemsDesktop : false,
          // itemsDesktopSmall : false,
          // itemsTablet: false,
          // itemsMobile : false
     
      });
     
    });


    // GO TO TOP
    $(function() {
    	$("#toTop").scrollToTop();
    });
    
});