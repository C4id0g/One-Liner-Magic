bucket_sort = lambda lst, num_buckets: [x for bucket in [sorted([x for x in lst if int(x * num_buckets) == i]) for i in range(num_buckets)] for x in bucket]