module.exports = function(grunt) {

    // 1. All configuration goes here 
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            dist: {
                src: [
                    'ag_iba/app/static/app/js/*.js' // All JS files in the JS folder
                ],
                dest: 'ag_iba/app/static/app/js/build/production.js',
            }
        },

        uglify: {
            build: {
                src: 'ag_iba/app/static/app/js/build/production.js',
                dest: 'ag_iba/app/static/app/js/build/production.min.js'
            }
        },

        imagemin: {
            dynamic: {
                files: [{
                    expand: true,
                    cwd: 'ag_iba/app/static/app/images/',
                    src: ['**/*.{png,jpg,gif}'],
                    dest: 'ag_iba/app/static/app/images/build/'
                }]
            }
        },

        watch: {
            options: {
                livereload: true,
            },
            scripts: {
                files: ['ag_iba/app/static/app/js/*.js'],
                tasks: ['concat', 'uglify'],
                options: {
                    spawn: false,
                },
            },
            css: {
                files: ['ag_iba/app/static/app/css/*.scss'],
                tasks: ['sass'],
                options: {
                    spawn: false,
                },
            },
        },

        sass: {
            dist: {
                options: {
                    style: 'compressed'
                },
                files: {
                    'ag_iba/app/static/app/css/build/global.css': 'ag_iba/app/static/app/css/global.scss'
                }
            }
        }
    });

    // 3. Where we tell Grunt we plan to use this plug-in.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-imagemin');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-sass');

    // 4. Where we tell Grunt what to do when we type "grunt" into the terminal.
    grunt.registerTask('default', ['concat', 'uglify', 'imagemin', 'watch', 'sass']);

};