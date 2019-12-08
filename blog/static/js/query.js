Splitting();


// class DirectionAwareShadow {
//   constructor({
//     target = null,
//     blur = 0,
//     spread = 0,
//     inset = false,
//     reverse = false,
//     color = 'currentColor',
//     offset = 1
//   } = {}) {
//     this.target = target ? document.querySelectorAll(target) : target;
//     this.blur = blur;
//     this.inset = inset;
//     this.spread = spread;
//     this.reverse = reverse;
//     this.color = color;
//     this.offset = offset;
//   }
//
//   move() {
//     this.target.forEach(t =>
//       t.addEventListener('mousemove', e => this.calc(e))
//     );
//   }
//
//   px(val) {
//     return `${val}px`;
//   }
//
//   calc(e) {
//     const { currentTarget, offsetX, offsetY } = e;
//     const { offsetHeight, offsetWidth } = currentTarget;
//     const { color, reverse, offset } = this;
//
//     const blur = this.px(this.blur);
//     const spread = this.px(this.spread);
//     const inset = this.inset ? 'inset' : '';
//
//     const x = ((offsetWidth / 2 - offsetX) * offset) / 2;
//     const y = ((offsetHeight / 2 - offsetY) * offset) / 2;
//
//     const h = this.px(!reverse ? x : x * -1);
//     const v = this.px(!reverse ? y : y * -1);
//
//     currentTarget.style.boxShadow = `${h} ${v} ${blur} ${spread} ${color} ${inset}`;
//   }
//
//   init() {
//     if (!this.target) {
//       console.error('[direction-aware shadow] • you should add a target')
//       return;
//     }
//
//     this.move();
//   }
// }
//
// const circle = new DirectionAwareShadow({
//   target: '.circle',
//   blur: 30,
//   spread: 0,
//   offset: .8,
//   color: 'rgba(79, 1, 119, 0.36)',
//   inset: false,
//   reverse: false
// });
//
// circle.init();
//
// // highlightjs
// hljs.initHighlightingOnLoad();


const flash = document.querySelector(".flash");
const states = [
  () => {
    flash.style.transition = "transform 1ms";
    flash.style.transform = "translateX(-196px) rotate(0deg)";
  },
  () => {
    flash.style.transition = "transform 700ms ease-in-out";
    setTimeout(() => {
      flash.style.transform = "translateX(-196px) rotate(-485deg)";
    }, 100);
  },
  () => (flash.style.transform = "translateX(-196px) rotate(-320deg)"),
  () => (flash.style.transform = "translateX(-196px) rotate(-375deg)"),
  () => (flash.style.transform = "translateX(-196px) rotate(-355deg)"),
  () => (flash.style.transform = "translateX(-196px) rotate(-360deg)")
];
let currentState = 0;
const animateToNextState = () => {
  requestAnimationFrame(() => {
    states[++currentState % states.length]();
  });
};
flash.addEventListener("transitionend", () => animateToNextState());
window.onload = () => {
  animateToNextState();
};
