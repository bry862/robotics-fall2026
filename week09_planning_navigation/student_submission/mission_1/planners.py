"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct


def bfs(ctx):
    if ctx.start == ctx.goal:
        return [ctx.start]

    queue = deque([ctx.start])
    parent = {ctx.start: None}

    while queue:
        current = queue.popleft()

        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        for nxt in ctx.expand(current, len(queue) + 1):
            if nxt not in parent:
                parent[nxt] = current
                queue.append(nxt)

    return [] 


def dfs(ctx):
    if ctx.start == ctx.goal:
        return [ctx.start]

    stack = [ctx.start]
    parent = {ctx.start: None}

    while stack:
        current = stack.pop()

        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        for nxt in reversed(ctx.expand(current, len(stack) + 1)):
            if nxt not in parent:
                parent[nxt] = current
                stack.append(nxt)

    return []


def iddfs(ctx):
    if ctx.start == ctx.goal:
        return [ctx.start]

    limit = 0

    while True:
        parent = {ctx.start: None}

        def depth_limited(current, depth, path):
            if current == ctx.goal:
                return reconstruct(parent, ctx.goal)

            if depth == limit:
                return None

            neighbours = ctx.expand(current, 1)

            for nxt in neighbours:
                if nxt not in path:
                    parent[nxt] = current
                    result = depth_limited(nxt, depth + 1, path | {nxt})

                    if result is not None:
                        return result

            return None

        result = depth_limited(ctx.start, 0, {ctx.start})

        if result is not None:
            return result

        limit += 1

def astar(ctx):
    if ctx.start == ctx.goal:
        return [ctx.start]

    heap = []
    heappush(heap, (ctx.heuristic(ctx.start), 0, ctx.start))

    parent = {ctx.start: None}
    best_g = {ctx.start: 0}

    while heap:
        priority, cost, current = heappop(heap)

        if cost != best_g[current]:
            continue

        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        for nxt in ctx.expand(current, len(heap) + 1):
            new_cost = cost + 1

            if nxt not in best_g or new_cost < best_g[nxt]:
                best_g[nxt] = new_cost
                parent[nxt] = current

                priority = new_cost + ctx.heuristic(nxt)
                heappush(heap, (priority, new_cost, nxt))

    return []
