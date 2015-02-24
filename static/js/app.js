"use strict";
  	    
angular.module('quadrado', [])
  .config(['$interpolateProvider', function($interpolateProvider){
     $interpolateProvider.startSymbol('{[');
     $interpolateProvider.endSymbol(']}');
  }])  		
  .controller('Control', ["$http", function($http){
     var self = this;
     var SIZE = 45;
     var GAP = 10;
     
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
       var requestList = [];
  	   if (value === 1){
         self.increase();
         requestList = {'init': self.end+1, 'end': GAP+self.end};
  	   } else {
         self.decrease();
         requestList = {'init': self.init-GAP, 'end': self.init-1};
       }
  	   $http.get('/numdata', {params: requestList})
          .then(function(resp){
  		     self.lt = resp.data['numList'];
  		     self.updateVar();
  		     }, function(err){
  		          console.log('hmmm error .. ; ', err);
  		        
  		     });
     };
  		    
  }]);
