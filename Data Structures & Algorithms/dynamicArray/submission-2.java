class DynamicArray {

    int capacity;
    int size;
    int[] array;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        size = 0;
        array = new int[capacity];
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
    }

    public void pushback(int n) {
        if(size == capacity) {
            resize();
        }
        array[size++] = n;
    }

    public int popback() {
        size--;
        int temp = array[size];
        return temp;
    }

    private void resize() {
        capacity = capacity * 2;
        int[] temp = new int[capacity];
        for(int i = 0; i < size; i++) {
            temp[i] = array[i];
        }
        array = temp;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
