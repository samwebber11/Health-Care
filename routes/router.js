var express = require('express');
var router = express.Router();
var User = require('../models/user');
var path = require('path');

// GET route for reading data
router.get('/', function (req, res, next) {
  return res.sendFile(path.join(__dirname + '/Health/index.html'));
});

//POST route for updating data
router.post('/', function (req, res, next) {
  // confirm that user typed same password twice
  if (req.body.password !== req.body.passwordConf) {
    var err = new Error('Passwords do not match.');
    err.status = 400;
    res.send("passwords dont match");
    return next(err);
  }

  if(req.body.email &&
    req.body.username &&
    req.body.password &&
    req.body.passwordConf){

    var userData = {
      email: req.body.email,
      username: req.body.username,
      password: req.body.password,
      gender: req.body.gender,
    }

    User.create(userData, function (error, user) {
      if (error) {
        return next(error);
      } else {
        req.session.userId = user._id;
        return res.redirect('/profile');
      }
    });

  } else if (req.body.logemail && req.body.logpassword) {
    User.authenticate(req.body.logemail, req.body.logpassword, function (error, user) {
      if (error || !user) {
        var err = new Error('Wrong email or password.');
        err.status = 401;
        return next(err);
      } else {
        req.session.userId = user._id;
        return res.redirect('/profile');
      }
    });
  } else {
    var err = new Error('All fields required.');
    err.status = 400;
    return next(err);
  }
})

// GET route after registering
router.get('/profile', function (req, res, next) {
  User.findById(req.session.userId)
    .exec(function (error, user) {
      if (error) {
        return next(error);
      } else {
        if (user === null) {
          var err = new Error('Not authorized! Go back!');
          err.status = 400;
          return next(err);
        } else {
          return res.sendFile(path.join(__dirname+'/profile.html'))
          // return res.send('<h1>Welcome To Arpan Health Care</h1>'+
          // user.username + '<h2>Your Email Id: </h2>' + user.email + '<br><a type="button" href="/history">History Of Your Diagonsis</a>'+'<br><a type="button" href="/symptoms">Enter Your Symptoms here</a>'+'<br><a type="button" href="/logout">Logout</a>')
        }
      }
    });
});

router.get('/symptoms',function(req,res,next) {
  User.findById(req.session.userId)
  .exec(function(error,user) {
    if(error) {
      return next(error);
    } else {
      return res.sendFile(path.join(__dirname+'/symptoms.html'));
    }
  })
})

router.get('/history',function (req,res,next) {
  User.findById(req.session.userId)
  .exec(function (error,user) {
    if(error) {
      return next(error);
    } else
    {
      const userHistory = user.history;
      console.log("sambhav");
      // return res.sendFile(path.join(__dirname + '/history.html'));
      return res.send('<h1>Welcome To Arpan</h1>'+'<br><h2>Your Previous History is displayed below</h2>'+userHistory);
    }
  })
});


// router.post('/symptoms',function (req,res,next))
// GET for logout logout
router.get('/logout', function (req, res, next) {
  if (req.session) {
    // delete session object
    req.session.destroy(function (err) {
      if (err) {
        return next(err);
      } else {
        return res.redirect('/');
      }
    });
  }
});

module.exports = router;