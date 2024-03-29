def gen_static_html():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PLA-Complexity</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f2f2f2;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }
        h1 {
            margin: 0;
        }
        main {
            padding: 20px;
        }
        table {
            width: 60%;
            border-collapse: collapse;
            color: #333;
            font-family: Arial, sans-serif;
            font-size: 14px;
            text-align: left;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            margin: auto;
            margin-top: 50px;
            margin-bottom: 50px;
        }
        table th {
            background-color: #ff9800;
            color: #fff;
            font-weight: bold;
            padding: 10px;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-top: 1px solid #fff;
            border-bottom: 1px solid #ccc;
        }
        table tr:nth-child(even) td {
            background-color: #f2f2f2;
        }

        table tr:hover td {
            background-color: #ffedcc;
        }
        table td {
            background-color: #fff;
            padding: 10px;
            border-bottom: 1px solid #ccc;
            font-weight: bold;
        }
    </style>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <!-- Include DataTables CSS -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.css">

    <!-- Include jQuery -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    
    <!-- Include DataTables JS -->
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.js"></script>

    <script>
        $(document).ready( function () {
            $('#sortable-table').DataTable();
        } );
    </script>
</head>
<body>
    <header>
        <h1>PLA-Complexity</h1>
    </header>
    <main>
        <section>
            <p>Here we present the PLA-complexity curves of all the genomes that we have used to study PLA-complexity of the genomic k-mer spectra in our paper: <a target="_blank" href="https://www.biorxiv.org/content/10.1101/2024.02.08.579510v1.abstract">"Abrar, Md Hasin, and Paul Medvedev. "PLA-complexity of k-mer multisets." bioRxiv (2024): 2024-02."</a>
             </p>
        </section>
        <section>
            <h2>Method</h2>
            <p>To explore the PLA-complexity across a diverse set of genomes, we downloaded a sample of RefSeq genomes that are complete and full, do not have any missing bases, and are longer than 10,000nt. Our dataset contained 549 genomes, representing the kingdoms of Virus, Bacteria, Archaea, and Fungi.
            The median genome length was 2.7 mil and the maximum was 63 mil. We used O'Rourke's algorithm, with \(k=21\), to obtain the PLA-complexity \(b\) for  \(\epsilon \in \{1, 2, 4, 8, \ldots, 1024\}\). We then fit a two parameter curve \(b = B \cdot N/\epsilon^\\alpha\) to each genome using  non-linear least squares regression (function nls in R).
            As a seed, we set \(\\alpha=1\) and \(B \cdot N\) equal to the number of segments for \(\epsilon=1\). We found the fits to be fairly accurate, albeit generally underpredicting the number of segments when the number is small (i.e. for large \(\epsilon\) ). </p>
        </section>
        <section>
            <h2>PLA-Complexity Curves</h2>
            <p>The following table includes the pla-complexity curves, kingdoms and the size of all the genomes that we used for comparison in our paper.</p>
            <table id="sortable-table" class="display">
                <thead>
                    <tr>
                        <th style="width:50%">Genome</th>
                        <th style="width:20%">Kingdom</th>
                        <th style="width:30%">Size</th>
                    </tr>
                </thead>
                <tbody>
'''

def get_dynamic_html(ref_seq_id, figure_path, kingdom, length):    
    return '''
                    <tr>
                        <td><a target="_blank" href="{}">{}</a></td>
                        <td>{}</td>
                        <td>{}</td>
                    </tr>            
'''.format(figure_path, ref_seq_id, kingdom, length)

def get_tail_html():
    return '''
                </tbody>
            </table>
        </section>
    </main>
</body>
</html>
'''

def process_html(csv_file):
    html_file = gen_static_html()
    import csv
    with open(csv_file) as f:
        lines = f.readlines()
    # for row in reader:
    #     print(row)
    for line in lines[1:]:
        vals = line.strip().split(",")
        ref_seq_id = vals[1].strip()
        kingdom = vals[2].strip()
        length = vals[4].strip()
        figure_path = "Figures/"+ref_seq_id[1:-1]+".png"
        html_file += get_dynamic_html(ref_seq_id[1:-1], figure_path, kingdom[1:-1], length)
    html_file += get_tail_html()

    with open("index.html", "w") as f:
        f.writelines(html_file)

def main():
    import sys
    csv_file = sys.argv[1]
    process_html(csv_file)

main()