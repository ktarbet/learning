```text
// These are notes and simple experiments to demonstrate Pinvoking of DSS types of data

    // https://learn.microsoft.com/en-us/dotnet/framework/interop/marshalling-different-types-of-arrays
    /*
     * https://learn.microsoft.com/en-us/archive/msdn-magazine/2004/october/net-column-p-invoke-revisited#S2

    When the runtime marshaler sees that your code is passing to native code a reference to a managed reference object, it automatically pins the object. What this means is that the object is put in a special state where the garbage collector will neither move the object in memory nor remove the object from memory. Pinned objects hurt the performance of the garbage collector, but they assure that the memory remains intact for the life of the native call; this is critical to the proper functioning of the native code.

     *https://docs.microsoft.com/en-us/dotnet/framework/interop/copying-and-pinning
     * Pinning is automatically performed during marshalling for objects such as String
     * the interop marshaller passes an array as In parameters by default.
     * 
     * Pinning is automatically performed during marshalling for objects such as String, 
     * however you can also manually pin memory using the GCHandle class.
     * 
     * 
     * https://learn.microsoft.com/en-us/dotnet/standard/native-interop/best-practices
     * 
     * using string to pass by value (const char* in Native)
     * 
     * 
     * https://learn.microsoft.com/en-us/dotnet/framework/interop/marshalling-different-types-of-arrays
     * Unless an array is explicitly marshalled by reference, the default behavior marshals 
     * the array as an In parameter. You can change this behavior by applying the InAttribute 
     * and OutAttribute attributes explicitly.
     * 
     * 
     * 
     * https://stackoverflow.com/questions/2218444/when-passing-a-managed-byte-array-through-pinvoke-to-be-filled-in-by-win32-do
     * 
     * The CLR will automatically pin references to managed objects when they cross the 
     * PInvoke boundary. As soon as the PInvoke function exits the reference will be unpinned.
     * So in situations like having a native function fill a byte[] no manually pinning is necessary 
     * because the object is only used by native code during the function call.
     * 
     * 
     * 
     * 
     */

```


```c
HECDSS_API int hec_dss_test_modify_arg(int *value) {

    *value = 123;
    return 0;
}
```

```csharp

    [DllImport("hecdss", ExactSpelling = true)]
    static extern int hec_dss_test_modify_arg(ref int value);
    
    public void modifyIntegerValue()
    {
      int x = 0;
      //GCHandle h = GCHandle.Alloc(x, GCHandleType.Pinned);
      //IntPtr ip = h.AddrOfPinnedObject();
      hec_dss_test_modify_arg(ref x);
      Console.WriteLine("x = " + x);
      Assert.AreEqual(123, x);
    }
```    

```c
HECDSS_API int hec_dss_test_string_const(const char* s, int size) {

    printf("string='%s'  length=%d\n", s,(int)strlen(s));
    return 0;
}
```

```csharp

    [DllImport("hecdss", ExactSpelling = true)]
    static extern int hec_dss_test_string_const(string str, int size);
```


```c
HECDSS_API int hec_dss_test_string_buffer(char* outStr, int size) {
    char* tmp = "abc";
    strcpy(outStr, tmp);
    return 0;
}
```

```csharp
[DllImport("hecdss")]
    static extern int hec_dss_test_string_buffer(StringBuilder outStr, int size);
    
    [TestMethod]
    public void modifyUsingStringBuilder()
    {
      //string s = "hello";
      //hec_dss_test_string_const(s, s.Length);

      StringBuilder sb = new StringBuilder(128);
      //sb.Append("zzzz");
      hec_dss_test_string_buffer(sb, sb.Capacity);
      Console.WriteLine("outStr = " + sb.ToString());
      Assert.AreEqual("abc",sb.ToString());
    }
    
```

```c
HECDSS_API int hec_dss_test_string_char(char* outStr, int size) {
    char* tmp = "DEF\0";
    
    strcpy(outStr, tmp);
    printf("outStr = '%s'\n", outStr);
    return 0;
}
```

```csharp
[DllImport("hecdss", ExactSpelling = true)]
    static extern int hec_dss_test_string_char(byte[] outStr, int size);


    [TestMethod]
    public void modifyStringUsingByteArray()
    {
      using ByteString bs = new ByteString(64);
      hec_dss_test_string_char(bs.Data, bs.Data.Length);
      var s = bs.ToString();
      Console.WriteLine("After call: s = " +s );
      
      Assert.AreEqual("DEF", s);
    }


```

```c
HECDSS_API int hec_dss_test_list_of_string(char* data, int rows, int columns) {

  char buff[1024];
  for (int i = 0; i < rows; i++)
  {
    sprintf(buff, "/Basin/River/Flow//1Day/item %d", i);
    printf("buff='%s'", buff);
    char* s = data+i*columns;
    stringCopy(s, columns, buff, strlen(buff));
    printf("s='%s'", s);
  }
  
  return 0;
}
```csharp
[DllImport("hecdss", ExactSpelling = true)]
    static extern int hec_dss_test_list_of_string(byte[] s, int numberOfStrings, int size);

    [TestMethod]
    public void TestModifyListOfStrings()
    {
      int numberOfStrings = 10;
      int size = 400;
      var array2 = ArrayPool<byte>.Shared.Rent(numberOfStrings * size);
      hec_dss_test_list_of_string(array2, numberOfStrings, size);

      for (int i = 0; i < numberOfStrings; i++)
      {
        string a = Encoding.ASCII.GetString(array2, i * size, 400);
        a = a.Trim('\0');
        String expectedString = "/Basin/River/Flow//1Day/item "+i;
        
        Assert.AreEqual(expectedString, a);
      }

      ArrayPool<byte>.Shared.Return(array2);
    }


    public void ByteToText_ASCII()
    {
      for (int i = 0; i < 128; i++)
      {
        byte b = (byte)i;
        var s = Encoding.ASCII.GetString(new byte[] { b });
        Console.WriteLine("i="+i+" s='"+s+"' :"+Convert.ToString(b, 2).PadLeft(8, '0'));
      }
      
    }

```


