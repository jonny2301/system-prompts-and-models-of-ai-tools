const watcherWrap = require('../watcherWrap');

describe('watcherWrap', () => {
  beforeEach(() => {
    global.validate = jest.fn(() => true);
    global.logSuccess = jest.fn();
    global.findPatch = jest.fn(async () => '');
    global.logFailure = jest.fn();
  });

  test('returns result and logs success when valid', async () => {
    const fn = jest.fn(async (x) => x + 1);
    const wrapped = watcherWrap(fn, 'test');

    const result = await wrapped(1);

    expect(result).toBe(2);
    expect(fn).toHaveBeenCalledWith(1);
    expect(validate).toHaveBeenCalledWith(2, 'test');
    expect(logSuccess).toHaveBeenCalled();
    expect(logFailure).not.toHaveBeenCalled();
  });

  test('returns error object and logs failure when function throws', async () => {
    const error = new Error('fail');
    const fn = jest.fn(async () => { throw error; });
    findPatch.mockResolvedValue('patch');
    const wrapped = watcherWrap(fn, 'test');

    const result = await wrapped();

    expect(result).toEqual({ error: 'fail', suggestion: 'patch' });
    expect(findPatch).toHaveBeenCalledWith('test', 'fail');
    expect(logFailure).toHaveBeenCalled();
    expect(logSuccess).not.toHaveBeenCalled();
  });
});
