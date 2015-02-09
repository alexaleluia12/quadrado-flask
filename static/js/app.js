"use strict";
  	    
angular.module('quadrado', [])
  .config(['$interpolateProvider', function($interpolateProvider){
     $interpolateProvider.startSymbol('{[');
     $interpolateProvider.endSymbol(']}');
  }])  		
  .controller('Control', ["$http", function($http){
     var self = this;
     var SIZE = 45;
            
  	 self.lt = window.numList;
  	 self.init = self.lt[0];
  	 self.end = self.lt[self.lt.length - 1]
  	 self.rotate = 0;
  	 self.rotateClass = '';
	    
  	 self.updateVar = function(){
  	   self.init = self.lt[0];
  	   self.end  = self.lt[self.lt.length - 1]
  	 };
  		    
  	 self.canShowBack = function(){
  	   return self.init > 1;
     };
  		    
  	 self.increase = function(){
  	   self.rotate += SIZE;
       self.rotateClass = "change";
     };
  		    
  		    
     self.decrease = function(){
       self.rotate -= SIZE;
  	 };
  		    
     self.get = function(value){
  	   if (value === 1){
         self.increase();
  	   } else {
         self.decrease();
       }
  	   $http.get('/numdata', {params:{'op': value}})
          .then(function(resp){
  		     self.lt = resp.data['numList'];
  		     self.updateVar();
  		     }, function(err){
  		          console.log('umm eroo aconteceu; ', err);
  		        
  		     })
     };
  		    
  }]);
