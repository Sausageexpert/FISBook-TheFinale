import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

document.addEventListener('DOMContentLoaded', function(){

    const scene = new THREE.Scene()
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
    camera.position.set(0,2,8);

    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);

    const scenebox = document.getElementById('scene-box');
    scenebox.appendChild(renderer.domElement);

    const earthTexture = new THREE.TextureLoader().load('/media/earth.jpg');
    const earth = new THREE.Mesh(
        new THREE.SphereGeometry(3, 32, 32),
        new THREE.MeshStandardMaterial({
            map: earthTexture
        })
    );

    scene.add(earth)

    function addStar(){
        const geometry = new THREE.SphereGeometry(0.25, 24, 24);
        const material = new THREE.MeshStandardMaterial({color: 0xffffff});
        const star = new THREE.Mesh(geometry, material);
    
        const [x,y,z] = Array(3).fill().map(()=> THREE.MathUtils.randFloatSpread(100));
        star.position.set(x, y, z);
        scene.add(star);
    }
    
    Array(250).fill().forEach(addStar)





    const directionalLight = new THREE.DirectionalLight(0xffffff, 1.2);
    directionalLight.position.x = 5;
    scene.add(directionalLight)


    const controls = new OrbitControls(camera, renderer.domElement)
    const animate = () => {
       // torus.rotation.x+=0.02;
        renderer.render(scene, camera);
        controls.update();
        requestAnimationFrame(animate);
        
    }

    document.body.onscroll = scrollFunction

    function scrollFunction(){
        earth.rotation.y+=0.05;
    }
    animate();


});