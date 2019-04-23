var _ = require('lodash') // 모듈 호출
var menus = ['짜장면', '짬뽕', '볶음밥'] // 배열 선언
var pick = _.sample(menus)
var object = { // 객체 선언
    "짜장면":'http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1214/IE002069160_STD.jpg',
    "짬뽕":'https://png.pngtree.com/element_origin_min_pic/00/00/11/095823383855d7e.jpg',
    "볶음밥":'http://food.chosun.com/site/data/img_dir/2012/08/08/2012080802054_0.jpg'
  }
console.log(object[pick])
//console.log(object['짜장면'])