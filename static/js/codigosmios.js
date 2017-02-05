var marker;

	function initMap() {
  		var map = new google.maps.Map(document.getElementById('map'), {
    		zoom: 13,
    		center: {lat: -3.988354, lng: -79.198303} 
  	});

  	marker = new google.maps.Marker({
    	map: map,
    	draggable: true,
    	animation: google.maps.Animation.DROP,
    	position: {lat: -3.988354, lng: -79.198303}
  	});
  		marker.addListener('click', toggleBounce);
	}


	function toggleBounce() {
  		if (marker.getAnimation() !== null) {
    		marker.setAnimation(null);
  		} else {
    		marker.setAnimation(google.maps.Animation.BOUNCE);
  		}
	}
	$(function(){
  	$(".slides").slidesjs({
    play: {
      active: true,
        // [boolean] Generate the play and stop buttons.
        // You cannot use your own buttons. Sorry.
      effect: "slide",
        // [string] Can be either "slide" or "fade".
      interval: 5000,
        // [number] Time spent on each slide in milliseconds.
      auto: true,
        // [boolean] Start playing the slideshow on load.
      swap: true,
        // [boolean] show/hide stop and play buttons
      pauseOnHover: false,
        // [boolean] pause a playing slideshow on hover
      restartDelay: 2500
        // [number] restart delay on inactive slideshow
    }
  });
});