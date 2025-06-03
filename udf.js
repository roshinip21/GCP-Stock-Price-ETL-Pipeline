function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.timestamp = values[0];
    obj.Open = values[1];
    obj.High = values[2];
    obj.Low = values[3];
    obj.Close = values[4];
    obj.Volume = values[5];
    obj.Open_Interes = values[6];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }