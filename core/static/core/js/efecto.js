var xmlns = "http://www.w3.org/2000/svg",
  xlinkns = "http://www.w3.org/1999/xlink",
  select = function(s) {
    return document.querySelector(s);
  },
  selectAll = function(s) {
    return document.querySelectorAll(s);
  },
    liquid1 = selectAll('.liquid1'),
    liquid2 = selectAll('.liquid2')
    tubeShine = select('.tubeShine'),
    label = select('.label'),
    follower = select('.follower'),
    dragger = select('.dragger'),
    dragTip = select('.dragTip'),
    minDragY = -380,
    liquidId = 0,
    step = Math.abs(minDragY/100),
    snap = Math.abs(minDragY/10),
    followerVY = 0
  

TweenMax.set('svg', {
  visibility: 'visible'
})

TweenMax.set(dragTip, {
 transformOrigin:'20% 50%'
})

var tl1 = new TimelineMax()
tl1.staggerTo(liquid1, 0.8, {
 x:'-=200',
 ease:Linear.easeNone,
 repeat:-1
})

var tl2 = new TimelineMax()
tl2.staggerTo(liquid2, 1.2, {
 x:'-=200',
 ease:Linear.easeNone,
 repeat:-1
})

tl.time(100);

document.addEventListener("touchmove", function(event){
    event.preventDefault();
});

