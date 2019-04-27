angular.module('app', ['ui.router'])
.config (function ($routeProvider){
	$routeProvider
        	.when('/', {controller:'allProducts', templateUrl: '/mainapp/templates/mainapp/allproducts.html'})
        	.when('/reception', {controller:'reception', templateUrl: '/mainapp/templates/mainapp/reception.html'})
        	.when('/kitchen', {controller:'kitchen', templateUrl: '/mainapp/templates/mainapp/kitchen.html'})
        	.when('/arch', {controller:'arch', templateUrl: '/mainapp/templates/mainapp/arch.html'})
        	.when('/special', {controller:'special', templateUrl: '/mainapp/templates/mainapp/special.html'})
        	.when('/tables', {controller:'tables', templateUrl: '/mainapp/templates/mainapp/tables.html'})
        	.when('/decor', {controller:'decor', templateUrl: '/mainapp/templates/mainapp/decor.html'})
        	.when('/living', {controller:'living', templateUrl: '/mainapp/templates/mainapp/living.html'})
	.otherwise({redirectTo: '/'});
})

.controller('menuRepeat', function($scope){
	$scope.menu = [
		{ name: 'приёмные зоны', url: '#/reception' },
		{ name: 'обеденные зоны', url: '#/kitchen' },
		{ name: 'системы хранения', url: '#/arch' },
		{ name: 'специализированная мебель', url: '#/special' },
		{ name: 'столешницы', url: '#/tables' },
		{ name: 'декоративные элементы', url: '#/decor' },
		{ name: 'в жилые помещения', url: '#/living' },
	]
})

.controller('allProducts', function($scope) {
        $scope.pics = [
		{'title' : 'Pict1', 'url' : 'img/all/slide1.jpg', 'type' : 'default' },
		{'title' : 'Pict2', 'url' : 'img/all/slide2.jpg', 'type' : 'title1'},
		{'title' : 'Pict3', 'url' : 'img/all/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict4', 'url' : 'img/all/slide4.jpg', 'type' : 'title3'}
	];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})
.controller('about', function($scope) {
	$scope.pics = [
		{'title' : 'Pict1', 'url' : 'img/about/slide1.jpg', 'type' : 'default' },
		{'title' : 'Pict2', 'url' : 'img/about/slide2.jpg', 'type' : 'title1'},
		{'title' : 'Pict3', 'url' : 'img/about/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict2', 'url' : 'img/about/slide2.jpg', 'type' : 'title1'},
                {'title' : 'Pict3', 'url' : 'img/about/slide3.jpg', 'type' : 'title2'},
		{'title' : 'Pict4', 'url' : 'img/about/slide4.jpg', 'type' : 'title3'}
	];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})
.controller('reception', function($scope) {$scope.pics = [
		{'title' : 'Pict1', 'url' : 'img/rec/slide1.jpg', 'type' : 'default' },
		{'title' : 'Pict2', 'url' : 'img/rec/slide2.jpg', 'type' : 'title1'},
		{'title' : 'Pict3', 'url' : 'img/rec/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict4', 'url' : 'img/rec/slide4.jpg', 'type' : 'title3'},
		{'title' : 'Pict5', 'url' : 'img/rec/slide5.jpg', 'type' : 'title4'},
		{'title' : 'Pict6', 'url' : 'img/rec/slide6.jpg', 'type' : 'title5'},
                {'title' : 'Pict7', 'url' : 'img/rec/slide7.jpg', 'type' : 'title6'},
                {'title' : 'Pict8', 'url' : 'img/rec/slide8.jpg', 'type' : 'title7'}
	];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})
.controller('kitchen', function($scope) {$scope.pics = [
		{'title' : 'Pict1', 'url' : 'img/kit/slide1.jpg', 'type' : 'default' },
		{'title' : 'Pict2', 'url' : 'img/kit/slide2.jpg', 'type' : 'title1'},
		{'title' : 'Pict3', 'url' : 'img/kit/slide3.jpg', 'type' : 'title2'},
		{'title' : 'Pict4', 'url' : 'img/kit/slide4.jpg', 'type' : 'title3'},
		{'title' : 'Pict5', 'url' : 'img/kit/slide5.jpg', 'type' : 'title4'},
                {'title' : 'Pict6', 'url' : 'img/kit/slide6.jpg', 'type' : 'title5'}
	];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})
.controller('arch', function($scope) {$scope.pics = [
		{'title' : 'Pict1', 'url' : 'img/arch/slide1.jpg', 'type' : 'default' },
		{'title' : 'Pict2', 'url' : 'img/arch/slide2.jpg', 'type' : 'title1'},
		{'title' : 'Pict3', 'url' : 'img/arch/slide3.jpg', 'type' : 'title2'},
		{'title' : 'Pict4', 'url' : 'img/arch/slide4.jpg', 'type' : 'title3'},
		{'title' : 'Pict5', 'url' : 'img/arch/slide5.jpg', 'type' : 'title4'},
                {'title' : 'Pict6', 'url' : 'img/arch/slide6.jpg', 'type' : 'title5'},
                {'title' : 'Pict7', 'url' : 'img/arch/slide7.jpg', 'type' : 'title6'},
	];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})

.controller('special', function($scope) {$scope.pics = [
                {'title' : 'Pict1', 'url' : 'img/spec/slide1.jpg', 'type' : 'default' },
                {'title' : 'Pict2', 'url' : 'img/spec/slide2.jpg', 'type' : 'title1'},
                {'title' : 'Pict3', 'url' : 'img/spec/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict4', 'url' : 'img/spec/slide4.jpg', 'type' : 'title3'},
                {'title' : 'Pict5', 'url' : 'img/spec/slide5.jpg', 'type' : 'title4'},
                {'title' : 'Pict6', 'url' : 'img/spec/slide6.jpg', 'type' : 'title5'},
                {'title' : 'Pict7', 'url' : 'img/spec/slide7.jpg', 'type' : 'title6'}
        ];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})

.controller('tables', function($scope) {$scope.pics = [
                {'title' : 'Pict1', 'url' : 'img/tables/slide1.jpg', 'type' : 'default' },
                {'title' : 'Pict2', 'url' : 'img/tables/slide2.jpg', 'type' : 'title1'},
                {'title' : 'Pict3', 'url' : 'img/tables/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict4', 'url' : 'img/tables/slide4.jpg', 'type' : 'title3'},
                {'title' : 'Pict5', 'url' : 'img/tables/slide5.jpg', 'type' : 'title4'},
                {'title' : 'Pict6', 'url' : 'img/tables/slide6.jpg', 'type' : 'title5'},
                {'title' : 'Pict7', 'url' : 'img/tables/slide7.jpg', 'type' : 'title6'},
                {'title' : 'Pict8', 'url' : 'img/tables/slide8.jpg', 'type' : 'title7'},
                {'title' : 'Pict9', 'url' : 'img/tables/slide9.jpg', 'type' : 'title8'}
        ];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})

.controller('decor', function($scope) {$scope.pics = [
                {'title' : 'Pict1', 'url' : 'img/decor/slide1.jpg', 'type' : 'default' },
                {'title' : 'Pict2', 'url' : 'img/decor/slide2.jpg', 'type' : 'title1'},
                {'title' : 'Pict3', 'url' : 'img/decor/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict4', 'url' : 'img/decor/slide4.jpg', 'type' : 'title3'},
                {'title' : 'Pict5', 'url' : 'img/decor/slide5.jpg', 'type' : 'title4'},
                {'title' : 'Pict6', 'url' : 'img/decor/slide6.jpg', 'type' : 'title5'},
                {'title' : 'Pict7', 'url' : 'img/decor/slide7.jpg', 'type' : 'title6'}
        ];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})

.controller('living', function($scope) {$scope.pics = [
                {'title' : 'Pict1', 'url' : 'img/living/slide1.jpg', 'type' : 'default' },
                {'title' : 'Pict2', 'url' : 'img/living/slide2.jpg', 'type' : 'title1'},
                {'title' : 'Pict3', 'url' : 'img/living/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict4', 'url' : 'img/living/slide4.jpg', 'type' : 'title3'}
        ];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})
.controller('add', function($scope) {$scope.pics = [
                {'title' : 'Pict1', 'url' : 'img/add/slide1.jpg', 'type' : 'default' },
                {'title' : 'Pict2', 'url' : 'img/add/slide2.jpg', 'type' : 'title1'},
                {'title' : 'Pict3', 'url' : 'img/add/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict2', 'url' : 'img/about/slide2.jpg', 'type' : 'title1'},
                {'title' : 'Pict3', 'url' : 'img/about/slide3.jpg', 'type' : 'title2'},
                {'title' : 'Pict4', 'url' : 'img/add/slide4.jpg', 'type' : 'title3'}
        ];$scope.searchType = $scope.pics[0];$scope.selectSearchType = function(list) {$scope.searchType = list;};
})