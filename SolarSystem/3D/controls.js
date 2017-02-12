window.addEventListener('DOMMouseScroll', MouseWheelFox, false);
window.addEventListener('mousewheel', MouseWheelHandler, false);
window.addEventListener('wheel', MouseWheelHandler, false);

function MouseWheelHandler( e ) {
	var dir = -e.deltaY/4000
	UpdateZoom( dir )
};
function MouseWheelFox( e ) {
	var dir = -e.detail/80
	UpdateZoom( dir )
};

function UpdateZoom( direction ) {
	if( direction > 0 ) { direction = 1 } else { direction = - 1 };
	if ( zoom > 400 && direction == -1 ) {
		return
	}
	console.log( direction )
	zoom -= Math.floor( direction * (zoom/10) )
	if ( zoom > maxzoom ) {
		maxzoom = zoom
		for (var i = 0; i < Math.floor(zoom/10); i++) {
			GeneratePlanetObject()
		}
		console.log( zoom )
	}
	
	for (var i = 0; i < planets.length; i++) {
		var c = (1 - (i/2/zoom)) - 0.5
		if ( c > 0.1 && zoom < 100 ) {
			planets[i].path.visible = true
			planets[i].path.material.color.setRGB( c, c, c )
		} else {
			planets[i].path.visible = false
		}
	}
	
	camera.position.z = zoom;
	camera.position.y = camera.position.z/3;
	
	camera.lookAt( new THREE.Vector3() );	
	
}