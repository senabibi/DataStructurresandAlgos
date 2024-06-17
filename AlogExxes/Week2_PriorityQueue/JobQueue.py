# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


import heapq

def assign_jobs(n_workers, jobs):
    result = []
    # Initialize the min-heap with all workers being free at time 0
    pq = [(0, i) for i in range(n_workers)]
    heapq.heapify(pq)

    for job in jobs:
        # Extract the next available worker
        next_free_time, next_worker = heapq.heappop(pq)
        result.append(AssignedJob(next_worker, next_free_time))
        # Add the worker back with the updated next free time
        heapq.heappush(pq, (next_free_time + job, next_worker))

    return result

# Rest of the main function remains the same



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()

