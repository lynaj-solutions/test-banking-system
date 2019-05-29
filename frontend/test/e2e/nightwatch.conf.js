require('babel-register')
var config = require('../../config')

// http://nightwatchjs.org/gettingstarted#settings-file
// module.exports = {
//   src_folders: ['test/e2e/specs'],
//   output_folder: 'test/e2e/reports',
//   custom_assertions_path: ['test/e2e/custom-assertions'],
//
//   selenium: {
//     start_process: true,
//     server_path: require('selenium-server').path,
//     host: '127.0.0.1',
//     port: 4444,
//     cli_args: {
//       'webdriver.chrome.driver': 'node_modules/.bin/chromedriver'
//     }
//   },
//   test_settings: {
//     default: {
//       selenium_port: 4444,
//       selenium_host: 'localhost',
//       silent: true,
//       globals: {
//         devServerURL: 'http://localhost:' + (process.env.PORT || config.dev.port)
//       }
//     },
//
//     chrome: {
//       desiredCapabilities: {
//         browserName: 'chrome',
//         "chromeOptions" : {
//            "args" : ["headless"]
//         },
//         javascriptEnabled: true,
//         acceptSslCerts: true
//       }
//     }
//   }
// }



module.exports = {

  src_folders: ['test/e2e/specs'],
  output_folder: 'test/e2e/reports',
  custom_assertions_path: ['test/e2e/custom-assertions'],

  "webdriver": {
    "start_process" : true,
    "server_path": "node_modules/.bin/geckodriver",
    "cli_args": [
      "--log", "debug"
    ],
    "port": 4444
  },

  "test_settings" : {
    "firefox" : {
      "desiredCapabilities": {
        "browserName" : "firefox",
        "acceptInsecureCerts": true,
        "alwaysMatch": {
          "moz:firefoxOptions": {
            "args":  ["-headless", "no-sandbox", "disable-gpu"]
          }
        }
      }
    }
  }


}
