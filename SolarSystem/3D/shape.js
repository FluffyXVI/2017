function CreateSpherePlanet( size, color ) {
	var geo = new THREE.SphereGeometry( size, 16, 16 )
	for ( var i = 0; i < geo.faces.length; i+=1 ) {
		var c = new THREE.Color( color ).addScalar( -i/1000 )
		geo.faces[ i ].color = c;
	}
	var mat = planetmaterial;
	return new THREE.Mesh( geo, mat );
}

function CreateCubicPlanet( size, color ) {
	var geo = new THREE.BoxGeometry( size, size, size );
	for ( var i = 0; i < geo.faces.length; i+=2 ) {
		var c = new THREE.Color( color ).addScalar( -i/48 )
		geo.faces[ i ].color = c;
		geo.faces[ i+1 ].color = c;
	}
	var mat = planetmaterial;
	return new THREE.Mesh( geo, mat );
}

function CreateOctaPlanet( size, color ) {
	var geo = new THREE.OctahedronGeometry( size );
	for ( var i = 0; i < geo.faces.length; i+=1 ) {
		var c = new THREE.Color( color ).addScalar( -i/24 )
		geo.faces[ i ].color = c;
	}
	var mat = planetmaterial;
	return new THREE.Mesh( geo, mat );
}

function CreateDoDecaPlanet( size, color ) {
	var geo = new THREE.DodecahedronGeometry( size );
	for ( var i = 0; i < geo.faces.length; i+=3 ) {
		var c = new THREE.Color( color ).addScalar( -i/88 )
		geo.faces[ i ].color = c;
		geo.faces[ i+1 ].color = c;
		geo.faces[ i+2 ].color = c;
	}
	var mat = planetmaterial;
	return new THREE.Mesh( geo, mat );
}

function CreateIcosaPlanet( size, color ) {
	var geo = new THREE.IcosahedronGeometry( size );
	for ( var i = 0; i < geo.faces.length; i+=1 ) {
		var c = new THREE.Color( color ).addScalar( -i/128 )
		geo.faces[ i ].color = c;
	}
	var mat = planetmaterial;
	return new THREE.Mesh( geo, mat );
}

var shapes = [ CreateCubicPlanet, CreateDoDecaPlanet, CreateIcosaPlanet, CreateOctaPlanet, CreateSpherePlanet ]
function RandomShapePlanet( size, color, star ) {
	var planet;
	planet = shapes[Math.floor(Math.random() * shapes.length)]( size, color )
	return planet;
}