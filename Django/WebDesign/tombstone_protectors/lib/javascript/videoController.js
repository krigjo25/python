 // Declearing the Variables for the media player.
var videoEl = document.getElementsByTagName('video') [0],  // comma defines a new variable
	playPausB = document.getElementById('pypse'),
	vidCtrl = document.getElementById('ctrls'),
	mute = document.getElementById('muteb'),
	time = document.getElementById('timer');

// Removing the html attribute 'controls', to avoid to sets of controllers
videoEl.removeAttribute('controls');
videoEl.addEventListener('canplaythrough', function () {
vidCtrl.classList.remove('hidden');
}, false);

 // If button clicked check if video element is playing / pauseing
playPausB.addEventListener('click', function () {
	if (videoEl.paused) {
		videoEl.play ();
	} else {
		videoEl.pause();
	}

}, false);

videoEl.addEventListener('play', function () {
	playPausB.classList.add('playing');
}, false);
videoEl.addEventListener('pause', function(){

	playPausB.classList.remove('playing');
}, false);

// On click check if muted property is true or false
mute.addEventListener('click', function() {
	if (videoEl.muted) {
		videoEl.muted = false;
	} else {
		videoEl.muted = true;
	}
}, false);

videoEl.addEventListener('volumechange', function() {
	if (videoEl.muted) {
		mute.classList.add('muted');
	} else {
		mute.classList.remove('muted');
	}
}, false);

 // Sets the video back to the first frame, when it's finished
videoEl.addEventListener('ended', function() {
	videoEl.currentTime = 0;
}, false);

videoEl.addEventListener('timeupdate', function(){
	timer.innerHTML = secondsToTime(videoEl.currentTime);
}, false);