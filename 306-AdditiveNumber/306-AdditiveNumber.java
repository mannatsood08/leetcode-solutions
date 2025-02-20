class NumArray {
    private int[] tree;
    private int[] arr;

    public NumArray(int[] nums) {
        arr = Arrays.copyOf(nums, nums.length);
        tree = new int[4 * nums.length];
        if (nums.length > 0) {
            build(1, 0, nums.length - 1);
        }
    }

    private void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            int left = node * 2;
            int right = node * 2 + 1;

            build(left, start, mid);
            build(right, mid + 1, end);
            tree[node] = tree[left] + tree[right];
        }
    }

    public void update(int index, int val) {
        if (arr.length > 0) {
            update(1, 0, arr.length - 1, index, val);
        }
    }

    private void update(int node, int start, int end, int index, int val) {
        if (start == end) {
            arr[start] = val;
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            if (index <= mid) {
                update(node * 2, start, mid, index, val);
            } else {
                update(node * 2 + 1, mid + 1, end, index, val);
            }
            tree[node] = tree[node * 2] + tree[node * 2 + 1];
        }
    }

    public int sumRange(int left, int right) {
        if (arr.length == 0) return 0;
        return query(1, 0, arr.length - 1, left, right);
    }

    private int query(int node, int start, int end, int L, int R) {
        if (R < start || end < L) return 0;
        if (L <= start && end <= R) return tree[node];

        int mid = (start + end) / 2;
        int left = query(node * 2, start, mid, L, R);
        int right = query(node * 2 + 1, mid + 1, end, L, R);

        return left + right;
    }
}