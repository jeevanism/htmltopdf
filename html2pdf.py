# Import necessary modules
import sys
from PySide6 import QtCore, QtWidgets, QtWebEngineCore, QtWebEngineWidgets, QtGui

# Function to convert a web page to PDF
def url_to_pdf(url, pdf):
    # Create a QApplication instance
    app = QtWidgets.QApplication(sys.argv)

    # Set desktop user agent string
    profile = QtWebEngineCore.QWebEngineProfile.defaultProfile()
    profile.setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

    # Create the QWebEngineView with viewport size
    view = QtWebEngineWidgets.QWebEngineView()
    view.resize(1920, 1080)  # Adjust viewport size as needed
    page = QtWebEngineCore.QWebEnginePage(view)

    # Callback function for handling print finished event
    def handle_print_finished(filename, status):
        print("finished", filename, status)
        app.quit()  # Quit the application after printing

    # Callback function for handling load finished event
    def handle_load_finished(status):
        if status:
            # Adjust print layout
            layout = QtGui.QPageLayout()  # Import from QtGui
            layout.setPageSize(QtGui.QPageSize.A4)  # Or desired page size
            layout.setOrientation(QtGui.QPageLayout.Landscape)  # If content is wider
            layout.setMargins(QtCore.QMarginsF(0, 0, 0, 0))  # Set zero margins
            page.printToPdf(pdf, layout)
        else:
            print("Failed to load page")
            app.quit()

    # Connect signals and load the page
    page.pdfPrintingFinished.connect(handle_print_finished)
    page.loadFinished.connect(handle_load_finished)
    page.load(QtCore.QUrl(url))

    # Start the application event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python application.py <url> <name_of_pdf_file>")
        sys.exit(1)

    # Extract URL and PDF file name from command-line arguments
    url = sys.argv[1]
    pdf = sys.argv[2]

    # Call the function to convert the web page to PDF
    url_to_pdf(url, pdf)
