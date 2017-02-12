var planetmaterial = new THREE.MeshBasicMaterial( { vertexColors: THREE.FaceColors } );
var zoom = 10
var maxzoom = zoom

function RandomRange( min, max ) {
	var cap = max - min + 1;
	return Math.floor((Math.random() * cap) + min);
}

function GeneratePlanetCube( size, color ) {
	var geo = new THREE.BoxGeometry( size, size, size );
	for ( var i = 0; i < geo.faces.length; i+=2 ) {
		var c = new THREE.Color( color ).addScalar( -i/48 )
		geo.faces[ i ].color = c;
		geo.faces[ i+1 ].color = c;
	}
	var mat = planetmaterial;
	return new THREE.Mesh( geo, mat );
}

function GenerateOrbitalPath( radius ) {
	var curve = new THREE.EllipseCurve(0, 0, radius, radius, 0, 2 * Math.PI, false, Math.PI);
	var path = new THREE.Path( curve.getPoints( 60 ) ).createPointsGeometry();
	var ellipse = new THREE.Line( path, new THREE.LineBasicMaterial( { color : 0x444444 } ) );
	ellipse.rotation.x = Math.PI / 2;
	ellipse.position.x = 0;
	scene.add( ellipse );
	return ellipse
}

var pcolors = [ "cadetblue", "chocolate", "coral", "cornflowerblue", "darkblue", "darkcyan",
			"darkgreen", "darkmagenta", "darkolivegreen", "darkseagreen", "dimgray",
			"firebrick", "goldenrod", "lightblue", "lightseagreen", "lightyellow",
			"mistyrose", "olivedrab", "seashell", "sienna", "skyblue", "wheat" ]
function GeneratePlanetObject() {
	var size = (Math.random() * 0.65) + 0.3;
	var radius = lastradius + (Math.random()*1.15) + 0.65;
	lastradius = radius
	var object = GeneratePlanetCube( size, pcolors[Math.floor(Math.random() * pcolors.length)])
	var planet = {
		size: size,
		radius: radius,
		speed: Math.random()*0.008 * 1/(radius*0.4) + 0.001,
		angle: Math.random() * 360,
		orbit: Math.random(),
		rotate: (Math.random()*0.1) + 0.015,
		object: object,
		path: GenerateOrbitalPath( radius )
	}
	planets.push( planet )
	scene.add( object );
	return planet
}

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
var canvas = new THREE.WebGLRenderer();
canvas.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( canvas.domElement );

var lastradius = 1
var planets = []

var cube = GeneratePlanetCube( 1, "orange" )
scene.add( cube );

for (var i = 0; i < zoom; i++) { 
	GeneratePlanetObject()
}

camera.position.z = zoom;
camera.position.y = camera.position.z/3;

camera.lookAt( new THREE.Vector3() );

var render = function () {
	requestAnimationFrame( render );
	if( typeof RenderAdditional == 'function') {
		RenderAdditional()
	}
	cube.rotation.y += 0.005;
	for (var i = 0; i < planets.length; i++) { 
		var p = planets[i]
		var o = p.object
		var t = p.orbit % 1
		o.position.x = Math.sin( t*Math.PI*2 ) * p.radius
		o.position.z = Math.cos( t*Math.PI*2 ) * p.radius
		o.rotation.y += p.rotate
		p.orbit += p.speed
		if (p.orbit > 1) {
			p.orbit -= 1
		}
	}
	canvas.render(scene, camera);
};

render();