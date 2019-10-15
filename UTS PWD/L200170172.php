<html>
    <?php
        error_reporting(E_ALL ^ E_NOTICE);
        $conn=mysqli_connect('localhost','root','','l200170172');

        $NIP=$_POST["NIP"];
        $Nama=$_POST["Nama"];
        $Fakultas=$_POST["Fakultas"];
        $Alamat=$_POST["Alamat"];

        $Submit=$_POST["Submit"];
        $Reset=$_POST["Reset"];

        if($Submit){
            if(NIP==''){
                echo"Masukan NIP";
            }elseif(Nama==''){
                echo"Masukan Nama";
            }elseif(Fakultas==''){
                echo"Masukan Fakultas";
            }elseif(Alamat==''){
                echo"Masukan Alamat";
            }else{
                $insert= "INSERT INTO dosen_genap (NIP, Nama, Fakultas, Alamat) VALUES('$NIP', '$Nama', '$Fakultas', '$Alamat')";
            mysqli_query($conn, $insert);
            echo"data berhasil ditambahkan";}}

        ?>
    <head><title>Data Mahasiswa</title></head>
    <body>
        <table>
            <form methode='POST' action='l200170172.php'>
                <tr>
                    <td>NIP</td>
                    <td>:</td>
                    <td><input type='text' name='nama' size='10' value='<?php echo $data_d[0] ?>'></td>
                </tr></br>
                <tr>
                    <td>Nama</td>
                    <td>:</td>
                   <td><input type='text' name='nama' size='50' value='<?php echo $data_d[1] ?>'></td>
                </tr></br>
                <tr>
                    <td>Fakultas</td>
                    <td>:</td>
                    <td><input type='text' name='fakultas' size='50' value='<?php echo $data_d[2] ?>'></td>
                </tr></br>
                <tr>
                    <td>Alamat</td>
                    <td>:</td>
                    <td><input type='text' name='alamat' size='100' value='<?php echo $data_d[3] ?>'></td>
                </tr></br>
                <tr>
                    <td><input type='Submit' name='submit'></td>
                    <td><input type='Reset' name='reset'></td>
                </tr>
            </form>
        </table>
        <table border='1' align='center'>
            </form method='POST' action='l200170172.php'>
                <tr>
                    <td>NIP</td>
                    <td>Nama</td>
                    <td>Fakultas</td>
                    <td>Alamat</td>
                </tr>
                <?php
                error_reporting(E_ALL ^ E_NOTICE);
                $cari = "SELECT * FROM l200170172";
                $hasil = mysqli_query($conn, $cari);
                while($data=mysqli_fetch_row($hasil)){
                    echo"
                        <tr>
                        <td>$data[0]</td>
                        <td>$data[1]</td>
                        <td>$data[2]</td>
                        <td>$data[3]</td>
                        </tr>";
                }
                ?>
            </form>
        </table>
    </body>
</html>