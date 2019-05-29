const path = require('path')
//
process.env.VUE_CLI_BABEL_TARGET_NODE = true;
process.env.VUE_CLI_BABEL_TRANSPILE_MODULES = true;
//
module.exports = {
  rootDir: path.resolve(__dirname, '../../'),
  moduleFileExtensions: [
    'js',
    'json',
    'vue'
  ],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1'
  },
  transform: {
    '^.+\\.js$': '<rootDir>/node_modules/babel-jest',
    '.*\\.(vue)$': '<rootDir>/node_modules/vue-jest',
    "^.+\\.(js|jsx)?$": "<rootDir>/node_modules/babel-jest"
  },
  transformIgnorePatterns: [
      "<rootDir>/node_modules/(?!(babel-jest|jest-vue-preprocessor)/)",
      "<rootDir>/node_modules/.*",
      "/node_modules/.*",
      "/app/node_modules/vue-stepper/(.*?)",
      "/app/node_modules/.*",
      "node_modules/(?!(babel-jest|jest-vue-preprocessor)/)"
  ],
  testPathIgnorePatterns: [
    '<rootDir>/test/e2e/specs'
  ],
  snapshotSerializers: ['<rootDir>/node_modules/jest-serializer-vue'],
  setupFiles: ['<rootDir>/test/unit/setup'],
  coverageDirectory: '<rootDir>/test/unit/coverage',
  collectCoverage: true,
  coverageReporters: ["html", "text-summary"],
  collectCoverageFrom: [
    'src/**/*.{js,vue}',
    '!src/main.js',
    '!src/router/index.js',
    '!**/node_modules/**'
  ]
};
