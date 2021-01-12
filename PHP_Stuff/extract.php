<?php

/* Data Extract Script -- David Nettleship 25/07/2019 */
/* A simple PHP script that allows the user to extract data from the uk_towns table on the database */
/* The data is then written to a csv, zipped and moved to a different directory */

$servername = "localhost";
$username = "root";
$password = "";
$db = "test";

// Create db connection
$conn = mysqli_connect("localhost", "root", "", "test");

// Check db connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

// Run SQL
$headers_sql = "
SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = N'uk_towns'
";

$extract_sql = "
SELECT *
FROM test.uk_towns
WHERE nuts_region = 'East Midlands'
";

$sql_header_results = mysqli_query($conn,$headers_sql);
$sql_results = mysqli_query($conn,$extract_sql);


// Create csv
if(mysqli_num_rows($sql_results) > 0){
	
	$csv = fopen('east_mids_export.csv','w');
	
	// Add headers
	while($data = mysqli_fetch_assoc($sql_header_results)){
		fputcsv($csv, $data, ",");
	}
	
	// Add rows
	while($row = mysqli_fetch_assoc($sql_results)){
		fputcsv($csv, $row, ",");
	}
	
	fclose($csv);
	$src = "east_mids_export.csv";
	$dest = "C:/wamp64/www/php_stuff/export/east_mids_export.zip";

    } else{
        echo "No records matching your parameters were found!";
    }

// Zip csv
$srcZip = "east_mids_export.zip";
$zip = new zipArchive();

if($zip->open('east_mids_export.zip',zipArchive::CREATE) === TRUE){
	$zip->addFile($src);
	$zip->close();
}

// Move file into export directory, remove from current location
copy($srcZip,$dest);
echo ("Copied extract to " . $dest . " successfully!");
unlink($src);
unlink($srcZip);

?>
