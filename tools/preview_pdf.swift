// Render every page of a PDF to PNG thumbnails for visual review.
// Usage: swift tools/preview_pdf.swift <input.pdf> <output_dir>
import AppKit
import PDFKit

let args = CommandLine.arguments
guard args.count == 3, let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
  print("Usage: swift tools/preview_pdf.swift <input.pdf> <output_dir>")
  exit(1)
}
let size = doc.page(at: 0)!.bounds(for: .mediaBox).size
print("pages: \(doc.pageCount) size: \(size)")  // 810x1013 pt == 1080x1350 px
for i in 0..<doc.pageCount {
  let image = doc.page(at: i)!.thumbnail(of: NSSize(width: 540, height: 675), for: .mediaBox)
  let rep = NSBitmapImageRep(data: image.tiffRepresentation!)!
  let url = URL(fileURLWithPath: "\(args[2])/p\(i + 1).png")
  try! rep.representation(using: .png, properties: [:])!.write(to: url)
}
