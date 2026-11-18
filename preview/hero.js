import * as THREE from './vendor/three.module.js';

// Deterministic six-second loop: the same scene powers the interactive preview
// and the GIF/PNG embedded in GitHub. No external textures or random assets.
const canvas = document.querySelector('canvas');
const renderer = new THREE.WebGLRenderer({canvas, antialias:true, alpha:true, preserveDrawingBuffer:true});
renderer.setPixelRatio(1);
renderer.setClearColor(0xf3f0e8,0);
renderer.outputColorSpace=THREE.SRGBColorSpace;
renderer.toneMapping=THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure=1.25;
const scene=new THREE.Scene();
const camera=new THREE.OrthographicCamera(-8,8,3,-3,.1,100);
camera.position.set(0,0,20);
scene.add(new THREE.HemisphereLight(0xffffff,0x62786e,3));
const key=new THREE.DirectionalLight(0xffefdb,4);key.position.set(-3,6,9);scene.add(key);
const rim=new THREE.DirectionalLight(0xc9f3e5,3);rim.position.set(6,-2,4);scene.add(rim);
const group=new THREE.Group();scene.add(group);
const mat=new THREE.MeshStandardMaterial({color:0x244c46,roughness:.32,metalness:.38});
const knot=new THREE.Mesh(new THREE.TorusKnotGeometry(1.18,.19,220,24,2,3),mat);group.add(knot);
const fine=new THREE.Mesh(new THREE.TorusKnotGeometry(1.18,.203,180,8,2,3),new THREE.MeshBasicMaterial({color:0x85ac9b,wireframe:true,transparent:true,opacity:.08}));group.add(fine);
const core=new THREE.Mesh(new THREE.IcosahedronGeometry(.60,0),new THREE.MeshStandardMaterial({color:0xc97759,roughness:.47,metalness:.12}));group.add(core);
const edges=new THREE.LineSegments(new THREE.EdgesGeometry(new THREE.IcosahedronGeometry(.607,0)),new THREE.LineBasicMaterial({color:0xf3d2b1,transparent:true,opacity:.6}));group.add(edges);
const orbit=new THREE.Group();orbit.rotation.set(.85,.2,.16);group.add(orbit);
const ring=new THREE.Mesh(new THREE.TorusGeometry(2,.015,8,180),new THREE.MeshStandardMaterial({color:0xc58565,metalness:.35,roughness:.4}));orbit.add(ring);
const bead=new THREE.Mesh(new THREE.SphereGeometry(.085,18,12),new THREE.MeshStandardMaterial({color:0xc96f51,metalness:.15,roughness:.25}));orbit.add(bead);
const ring2=new THREE.Mesh(new THREE.TorusGeometry(2.18,.006,5,180),new THREE.MeshBasicMaterial({color:0x739184,transparent:true,opacity:.32}));ring2.rotation.set(.1,1.25,0);group.add(ring2);
const pointer={x:0,y:0};let manual=false;
window.addEventListener('pointermove',e=>{pointer.x=(e.clientX/innerWidth-.5)*.12;pointer.y=(e.clientY/innerHeight-.5)*.12;});
function resize(){const w=innerWidth,h=innerHeight;renderer.setSize(w,h,false);const a=w/h;camera.left=-3*a;camera.right=3*a;camera.updateProjectionMatrix();group.position.x=3.3;group.scale.setScalar(1.08);const overlay=document.querySelector('#overlay');overlay.style.transform=`scale(${w/1200})`;overlay.style.top=`${(h-420*w/1200)/2}px`;}
window.addEventListener('resize',resize);resize();
function renderAt(t){const angle=t/6*Math.PI*2;group.rotation.set(.18+.06*Math.sin(angle)+pointer.y,-.2+.12*Math.cos(angle)+pointer.x,-.18);knot.rotation.z=angle;fine.rotation.z=angle;core.rotation.set(angle,-angle,.3);edges.rotation.copy(core.rotation);bead.position.set(2*Math.cos(angle),2*Math.sin(angle),0);renderer.render(scene,camera);}
window.renderAt=t=>{manual=true;pointer.x=pointer.y=0;renderAt(t);};
window.sceneReady=true;
const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
function frame(ms){if(!manual)renderAt(reduced?0:(ms/1000)%6);requestAnimationFrame(frame);}requestAnimationFrame(frame);
