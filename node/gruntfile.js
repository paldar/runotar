module.exports = function(grunt) {

    var jshintFilePatterns = [
        "include/*.js",
        "lib/*.js",
    ];

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    uglify: {
        options: {
            banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
        },
        build: {
            src: 'src/<%= pkg.name %>.js',
            dest: 'build/<%= pkg.name %>.min.js'
        }
    },
    /*
    jshint: {
        all: {
            src: jshintFilePatterns,
        },
        options: {
            jshintrc: true,
            verbose: true
        }
    }
    */
    jshint: {
        files: jshintFilePatterns,
        options: {
            jshintrc: true,
            verbose: true
        }
    }
  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-jshint');

  // Default task(s).
  grunt.registerTask('default', ['jshint']);

};

