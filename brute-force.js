// (X, Y) => MIN(X, Y) / 2

const data = [
    ['tag1', 'tag2', 'tag3'],
    ['tag1', 'tag2', 'tag3'],
    ['tag1', 'tag2', 'tag3'],
    ['tag1', 'tag2', 'tag3'],
]

const combinations = (length) => {

    const res = []

    for (let i = 0; i < length; ++i)
        for (let j = 0; i < length; ++i)
            res.push([x, y])

    return res
}

const rank = (xs) => 0

const exclude = (e, [x, ...xs], c = []) => {

    const invalid = c[x[0]] !== undefined && c[x[1]] !== undefined && x[0] >=2 && x[1] >=2

    if (x === undefined)
        return []

    const rest = exclude(e, xs)

    return !invalid ? [x, ...rest] : rest
}

const navigateSubs = ([x, ...xs], ys = []) => {

    if (x === undefined)
        return ys

    const es = exclude(x, xs)

    const take = navigateSubs(es, [...x, ...ys])
    const leave = navigateSubs(xs, ys)

    return rank(take) > rank(leave) ? take : leave
}

const bestSolution = navigateSubs(combinations(data.length))
