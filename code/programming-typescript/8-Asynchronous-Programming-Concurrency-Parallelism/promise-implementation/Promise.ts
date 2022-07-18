type Executor<T> = (resolve: (result: T) => void, reject: (error: unknown) => void) => void;

export class MyPromise<ResultType> {
	constructor(executor: Executor<ResultType>) {}

	then<T>(thenFunc: (promisedResult: ResultType) => MyPromise<T>): MyPromise<T> {}

	catch<T>(catchFunc: (error: F) => MyPromise<T>): MyPromise<T> {}
}
