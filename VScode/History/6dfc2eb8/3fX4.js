
const { default: TestRunner } = require('jest-runner');
const jestTest = require('./jestTest');


test('returns the number plus 5', () => {
	expect(jestTest(1)).toBe(6);
})